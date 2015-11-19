
#ifndef PHONEBOOK_H_
#define PHONEBOOK_H_

typedef struct name {
  int id;
  char *name;
} name;

typedef struct number {
  int id;
  char *number;
  int name_id;
} number;

#endif
