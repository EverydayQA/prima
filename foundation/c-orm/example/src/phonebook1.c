
#include "isti.h"
#include "isti_sqlite.h"
#include "isti_str.h"
#include "isti_array.h"
#include "isti_db.h"

#include "phonebook.h"
#include "phonebook.corm.h"

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

static void find_name(isti_db *db, const char *text, name** name) {
  corm_name_select *select;
  *name = NULL;
  corm_name_select_alloc(&select, db);
  select->name(select, "like", text)->_go_one(select, name);
  select->_free(select, 0);
}

static void add_name(isti_db *db, const char *text, name** name) {
  corm_name_insert *insert;
  *name = calloc(1, sizeof(**name));
  (*name)->name = isti_str_char_dup(text);
  corm_name_insert_alloc(&insert, db);
  insert->id_key(insert)->_go_one(insert, *name);
  insert->_free(insert, 0);
}

static void search(isti_db *db, const char *text) {
  name *name;
  corm_number_select *select;
  corm_number_array *numbers;
  find_name(db, text, &name);
  if (name) {
    corm_number_select_alloc(&select, db);
    select->name_id(select, "=", name->id)->_go_any(select, &numbers);
    for (int i = 0; i < numbers->n.used; ++i)
      printf("%s: %s\n", name->name, numbers->number[i]->number);
  } else {
    printf(" No entry found for %s\n", text);
  }
  corm_name_free(name, 0);
  select->_free(select, 0);
  corm_number_array_free(numbers, 0);
}

static void add_number(isti_db *db, const char *text1, const char *text2) {
  name *name;
  number *number;
  corm_number_insert *insert;
  find_name(db, text1, &name);
  if (!name) add_name(db, text1, &name);
  number = calloc(1, sizeof(*number));
  number->name_id = name->id;
  number->number = isti_str_char_dup(text2);
  corm_number_insert_alloc(&insert, db);
  insert->id_key(insert)->_go_one(insert, number);
  corm_name_free(name, 0);
  corm_number_free(number, 0);
  insert->_free(insert, 0);
}

static void remove_number(isti_db *db, const char *text1, const char *text2) {
  name *name;
  corm_number_delete *delete;
  find_name(db, text1, &name);
  if (name) {
    corm_number_delete_alloc(&delete, db);
    delete->name_id(delete, "=", name->id)->number(delete, "like", text2+1)->_go(delete);
  }
  corm_name_free(name, 0);
  delete->_free(delete, 0);
}

static void user_loop(isti_db *db) {
  char *line = NULL;
  isti_chars_array *words;
  size_t size;
  printf("\n\\help for help\n\n");
  for (;;) {
    printf("> ");
    if (getline(&line, &size, stdin) < 0) break;
    isti_str_split(&words, line, " \n", 2);
    switch(words->n.used) {
    case 0:
      break;
    case 1:
      if (words->c[0][0] == '\\') {command(words->c[0]);}
      else {search(db, words->c[0]);}
      break;
    case 2:
      if (words->c[1][0] == '-') {remove_number(db, words->c[0], words->c[1]);}
      else {add_number(db, words->c[0], words->c[1]);}
      break;
    }
    isti_chars_array_free(words, 0);
  }
  free(line);
}

static void build_database(isti_db *db) {
  isti_str *ddl;
  isti_str_alloc(&ddl);
  isti_str_joinn(ddl, " ",
      "create table if not exists name (",
        "id integer primary key autoincrement,",
        "name text",
      ");",
      NULL);
  isti_str_joinn(ddl, " ",
      "create table if not exists number (",
        "id integer primary key autoincrement,",
        "number integer,",
        "name_id integer",
          "references name (id)",
          "on delete cascade",
      ");",
      NULL);
  db->str(db, ddl->c);
  isti_str_free(ddl, 0);
}

int main() {
  isti_db *db;
  isti_sqlite_open(&db, "/tmp/phonebook", 10);
  build_database(db);
  user_loop(db);
  db->close(db, 0);
}
