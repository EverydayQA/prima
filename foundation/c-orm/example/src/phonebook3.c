
#include "isti.h"
#include "isti_sqlite.h"
#include "isti_str.h"
#include "isti_array.h"
#include "isti_db.h"

ISTI_SQLITE_AS(sqlite)
ISTI_STR_AS(str)
ALIAS_ARRAY_AS(isti_chars_array, chars);

#include "phonebook.h"
#include "phonebook.corm.h"

CORM_NAME_AS(cname)
CORM_NUMBER_AS(cnumber)
ALIAS_ARRAY_AS(corm_number_array, cnumbers);

static int command(const char *cmd) {
  if (strcmp(cmd, "\\help")) {
    printf("unknown command %s\n", cmd);
  } else {
    printf("\nUsage:\n\
  \\help\n\
    Show this message\n\
  name\n\
    Search for numbers\n\
  name number\n\
    Add a number\n\
  name -number\n\
    Remove a number\n\
  ^D\n\
    Quit\n\n");
  }
  return 0;
}

static int find_name(isti_db *db, const char *text, name** name) {
  corm_name_select *select = NULL;
  *name = NULL;
  STATUS;
  CHECK(cname.select(&select, db));
  CHECK(select->name(select, "like", text)->_go_one(select, name));
  EXIT;
  if (status == ISTI_ERR_NO_RESULT) status = ISTI_OK; // see NULL name
  if (select) status = select->_free(select, status);
  RETURN;
}

static int add_name(isti_db *db, const char *text, name** name) {
  corm_name_insert *insert = NULL;
  STATUS;
  ASSERT_MEM(*name = calloc(1, sizeof(**name)));
  ASSERT_MEM((*name)->name = str.char_dup(text));
  CHECK(cname.insert(&insert, db));
  CHECK(insert->id_key(insert)->_go_one(insert, *name));
  EXIT;
  if (insert) status = insert->_free(insert, status);
  RETURN;
}

static int search(isti_db *db, const char *text) {
  name *name = NULL;
  corm_number_select *select = NULL;
  corm_number_array *numbers = NULL;
  STATUS;
  CHECK(find_name(db, text, &name));
  if (name) {
    CHECK(cnumber.select(&select, db));
    CHECK(select->name_id(select, "=", name->id)->_go_any(select, &numbers));
    for (int i = 0; i < numbers->n.used; ++i)
      printf("%s: %s\n", name->name, numbers->number[i]->number);
  } else {
    printf(" No entry found for %s\n", text);
  }
  EXIT;
  if (name) status = cname.free(name, status);
  if (select) status = select->_free(select, status);
  if (numbers) status = cnumbers.free(numbers, status);
  RETURN;
}

static int add_number(isti_db *db, const char *text1, const char *text2) {
  name *name = NULL;
  number *number = NULL;
  corm_number_insert *insert = NULL;
  STATUS;
  CHECK(find_name(db, text1, &name));
  if (!name) CHECK(add_name(db, text1, &name));
  ASSERT_MEM(number = calloc(1, sizeof(*number)));
  number->name_id = name->id;
  ASSERT_MEM(number->number = str.char_dup(text2));
  CHECK(cnumber.insert(&insert, db));
  CHECK(insert->id_key(insert)->_go_one(insert, number));
  EXIT;
  if (name) status = cname.free(name, status);
  if (number) status = cnumber.free(number, status);
  if (insert) status = insert->_free(insert, status);
  RETURN;
}

static int remove_number(isti_db *db, const char *text1, const char *text2) {
  name *name = NULL;
  corm_number_delete *delete = NULL;
  STATUS;
  CHECK(find_name(db, text1, &name));
  if (name) {
    CHECK(cnumber.delete(&delete, db));
    CHECK(delete->name_id(delete, "=", name->id)->number(delete, "like", text2+1)->_go(delete));
  }
  EXIT;
  if (name) status = cname.free(name, status);
  if (delete) status = delete->_free(delete, status);
  RETURN;
}

static int user_loop(isti_db *db) {
  char *line = NULL;
  isti_chars_array *words = NULL;
  size_t size;
  STATUS;
  printf("\n\\help for help\n\n");
  for (;;) {
    printf("> ");
    if (getline(&line, &size, stdin) < 0) break;
    CHECK(str.split(&words, line, " \n", 2));
    switch(words->n.used) {
    case 0:
      break;
    case 1:
      if (words->c[0][0] == '\\') {CHECK(command(words->c[0]));}
      else {CHECK(search(db, words->c[0]));}
      break;
    case 2:
      if (words->c[1][0] == '-') {CHECK(remove_number(db, words->c[0], words->c[1]));}
      else {CHECK(add_number(db, words->c[0], words->c[1]));}
      break;
    }
    CHECK(chars.free(words, status));
  }
  EXIT;
  if (line) free(line);
  RETURN;
}

static int build_database(isti_db *db) {
  isti_str *ddl = NULL;
  STATUS;
  CHECK(str.alloc(&ddl));
  CHECK(str.joinn(ddl, " ",
      "create table if not exists", cname.NAME, "(",
        cname.c.ID, cname.c.ID_type, "primary key autoincrement,",
        cname.c.NAME, cname.c.NAME_type,
      ");",
      NULL));
  CHECK(str.joinn(ddl, " ",
      "create table if not exists", cnumber.NUMBER, "(",
        cnumber.c.ID, cnumber.c.ID_type, "primary key autoincrement,",
        cnumber.c.NUMBER, cnumber.c.NUMBER_type, ",",
        cnumber.c.NAME_ID, cnumber.c.NAME_ID_type,
          "references", cname.NAME, "(", cname.c.ID, ")",
          "on delete cascade",
      ");",
      NULL));
  CHECK(db->str(db, ddl->c));
  EXIT;
  if (ddl) status = str.free(ddl, status);
  RETURN;
}

int main() {
  isti_db *db = NULL;
  STATUS;
  CHECK(sqlite.open(&db, "/tmp/phonebook", 10));
  CHECK(build_database(db));
  CHECK(user_loop(db));
  EXIT;
  if (db) status = db->close(db, status);
  if (status) printf("error: %d\n", status);
  RETURN;
}
