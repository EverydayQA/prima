
# This is the Python code that generates the C library to read a particular
# struct from the database.  It's surprisingly simple - all that is does is
# populate a `pystache` template from data previously constructed by parsing
# the C struct definition (see `parse.py`).

from __future__ import print_function

from pystache import render


def add_upper(params):
    for (key, value) in list(params.items()):
        if key == 'fields':
            for field in value: add_upper(field)
        else:
            try:
                params['upper_%s' % key] = value.upper()
            except AttributeError:
                pass

def build_data(params, struct=None):
    data = dict(params)
    if struct: data.update(struct)
    add_upper(data)
    return data

def generate_h_preamble(out, **params):
    print(render('''
#ifndef ISTI_COND_{{{ upper_root }}}_H_
#define ISTI_COND_{{{ upper_root }}}_H_

#include "isti_corm.h"
#include "isti_cond.h"
#include "isti_ins.h"
#include "isti_mem.h"
#include "isti_array.h"

#include "{{{ original }}}"
        ''', build_data(params)), file=out)

def generate_h_postamble(out, **params):
    print(render('''
#endif
        ''', build_data(params)), file=out)

def generate_h(struct, out, **params):
    print(render('''
// {{{ sname }}}


// mapping structs to and from the database

int {{{ prefix }}}_{{{ sname }}}_read_one(void *v, size_t n, char t, void *y);
int {{{ prefix }}}_{{{ sname }}}_read_any(void *v, size_t n, char t, void *y);
int {{{ prefix }}}_{{{ sname }}}_free({{{ sname }}} *ptr, int previous);
int {{{ prefix }}}_{{{ sname }}}_free_data(void *data, size_t n, int previous);


// struct and functions to handle arrays of the mapped type

ISTI_ARRAY_STRUCT_T({{{ prefix }}}_{{{ sname }}}_array, {{{ sname }}}*, {{{ sname }}});
ISTI_ARRAY_FNS_T({{{ prefix }}}_{{{ sname }}}_array, a, {{{ sname }}}*)
ISTI_ARRAY_FNS_H({{{ prefix }}}_{{{ sname }}}_array)

typedef int {{{ prefix }}}_{{{ sname }}}_free_t({{{ sname }}} *value, int previous);
{{{ prefix }}}_{{{ sname }}}_free_t {{{ prefix }}}_{{{ sname }}}_free;

typedef struct {{{ prefix }}}_{{{ sname }}}_array_fn {
  ISTI_ARRAY_FNS_R({{{ prefix }}}_{{{ sname }}}_array)
} {{{ prefix }}}_{{{ sname }}}_array_fn;


// general (corm-level) functions for adding table and column names to SQL

{{ #fields }}
ISTI_COND_PARAM_T({{{ prefix }}}_{{{ sname }}}_column_{{{ fname }}}, {{{ code }}}, {{{ type }}} {{ #pointer }}*{{ /pointer }})
ISTI_COND_PARAMS_T({{{ prefix }}}_{{{ sname }}}_columns_{{{ fname }}}, {{{ code }}}, {{{ type }}} {{ #pointer }}*{{ /pointer }})
ISTI_COND_PARAM_H({{{ prefix }}}_{{{ sname }}}_column_{{{ fname }}})
ISTI_COND_PARAMS_H({{{ prefix }}}_{{{ sname }}}_columns_{{{ fname }}})
ISTI_COND_PARAM_T({{{ prefix }}}_{{{ sname }}}_column_{{{ sname }}}_{{{ fname }}}, {{{ code }}}, {{{ type }}} {{ #pointer }}*{{ /pointer }})
ISTI_COND_PARAMS_T({{{ prefix }}}_{{{ sname }}}_columns_{{{ sname }}}_{{{ fname }}}, {{{ code }}}, {{{ type }}} {{ #pointer }}*{{ /pointer }})
ISTI_COND_PARAM_H({{{ prefix }}}_{{{ sname }}}_column_{{{ sname }}}_{{{ fname }}})
ISTI_COND_PARAMS_H({{{ prefix }}}_{{{ sname }}}_columns_{{{ sname }}}_{{{ fname }}})
{{ /fields }}

typedef struct {{{ prefix }}}_{{{ sname }}}_columns {
  {{ #fields }}
  char *{{{ upper_fname }}};
  char *{{{ upper_fname }}}_type;
  ISTI_COND_PARAM_R({{{ prefix }}}_{{{ sname }}}_column_{{{ fname }}}, {{{ fname }}})
  ISTI_COND_PARAMS_R({{{ prefix }}}_{{{ sname }}}_columns_{{{ fname }}}, {{{ fname }}})
  char *{{{ sname }}}_{{{ upper_fname }}};
  ISTI_COND_PARAM_R({{{ prefix }}}_{{{ sname }}}_column_{{{ sname }}}_{{{ fname }}}, {{{ sname }}}_{{{ fname }}})
  ISTI_COND_PARAMS_R({{{ prefix }}}_{{{ sname }}}_columns_{{{ sname }}}_{{{ fname }}}, {{{ sname }}}_{{{ fname }}})
  {{ /fields }}
} {{{ prefix }}}_{{{ sname }}}_columns;


// struct and functions to implement select (delegating some to columns defined above)

struct {{{ prefix }}}_{{{ sname }}}_select;

ISTI_CORM_SELECTS_T({{{ prefix }}}_{{{ sname }}}, {{{ sname }}}, {{{ prefix }}}_{{{ sname }}}_array)
{{ #fields }}
typedef struct {{{ prefix }}}_{{{ sname }}}_select *{{{ prefix }}}_{{{ sname }}}_select_param_{{{ fname }}}_t(struct {{{ prefix }}}_{{{ sname }}}_select *, const char *, const {{{ type }}} {{ #pointer }}*{{ /pointer }}{{{ fname }}});
typedef struct {{{ prefix }}}_{{{ sname }}}_select *{{{ prefix }}}_{{{ sname }}}_select_params_{{{ fname }}}_t(struct {{{ prefix }}}_{{{ sname }}}_select *, const char *, const {{{ type }}} {{ #pointer }}*{{ /pointer }}*{{{ fname }}}, size_t n);
{{ /fields }}

ISTI_CORM_SELECT_ALLOC_H({{{ prefix }}}_{{{ sname }}})

typedef struct {{{ prefix }}}_{{{ sname }}}_select {
  isti_db *_db;
  isti_cond *_cond;
  ISTI_CORM_SELECTS_R({{{ prefix }}}_{{{ sname }}})
  ISTI_CORM_LITERALS_R({{{ prefix }}}_{{{ sname }}}_select)
  {{ #fields }}
  {{{ prefix }}}_{{{ sname }}}_select_param_{{{ fname }}}_t *{{{ fname }}};
  {{{ prefix }}}_{{{ sname }}}_select_params_{{{ fname }}}_t *{{{ fname }}}_;
  {{{ prefix }}}_{{{ sname }}}_select_param_{{{ fname }}}_t *{{{ sname }}}_{{{ fname }}};
  {{{ prefix }}}_{{{ sname }}}_select_params_{{{ fname }}}_t *{{{ sname }}}_{{{ fname }}}_;
  {{ /fields }}
} {{{ prefix }}}_{{{ sname }}}_select;


// struct and functions to implement delete (very similar to select above)

struct {{{ prefix }}}_{{{ sname }}}_delete;

ISTI_CORM_DELETES_T({{{ prefix }}}_{{{ sname }}}, {{{ sname }}}, {{{ prefix }}}_{{{ sname }}}_array)
{{ #fields }}
typedef struct {{{ prefix }}}_{{{ sname }}}_delete *{{{ prefix }}}_{{{ sname }}}_delete_param_{{{ fname }}}_t(struct {{{ prefix }}}_{{{ sname }}}_delete *, const char *, const {{{ type }}} {{ #pointer }}*{{ /pointer }}{{{ fname }}});
typedef struct {{{ prefix }}}_{{{ sname }}}_delete *{{{ prefix }}}_{{{ sname }}}_delete_params_{{{ fname }}}_t(struct {{{ prefix }}}_{{{ sname }}}_delete *, const char *, const {{{ type }}} {{ #pointer }}*{{ /pointer }}*{{{ fname }}}, size_t n);
{{ /fields }}

ISTI_CORM_DELETE_ALLOC_H({{{ prefix }}}_{{{ sname }}})

typedef struct {{{ prefix }}}_{{{ sname }}}_delete {
  isti_db *_db;
  isti_cond *_cond;
  ISTI_CORM_DELETES_R({{{ prefix }}}_{{{ sname }}})
  ISTI_CORM_LITERALS_R({{{ prefix }}}_{{{ sname }}}_delete)
  {{ #fields }}
  {{{ prefix }}}_{{{ sname }}}_delete_param_{{{ fname }}}_t *{{{ fname }}};
  {{{ prefix }}}_{{{ sname }}}_delete_params_{{{ fname }}}_t *{{{ fname }}}_;
  {{{ prefix }}}_{{{ sname }}}_delete_param_{{{ fname }}}_t *{{{ sname }}}_{{{ fname }}};
  {{{ prefix }}}_{{{ sname }}}_delete_params_{{{ fname }}}_t *{{{ sname }}}_{{{ fname }}}_;
  {{ /fields }}
} {{{ prefix }}}_{{{ sname }}}_delete;


// struct and functions to implement insert

struct {{{ prefix }}}_{{{ sname }}}_insert;

ISTI_CORM_INSERTS_T({{{ prefix }}}_{{{ sname }}}, {{{ sname }}}, {{{ prefix }}}_{{{ sname }}}_array)
{{ #fields }}
typedef struct {{{ prefix }}}_{{{ sname }}}_insert *{{{ prefix }}}_{{{ sname }}}_key_{{{ fname }}}_t(struct {{{ prefix }}}_{{{ sname }}}_insert *);
{{ /fields }}

ISTI_CORM_INSERT_ALLOC_H({{{ prefix }}}_{{{ sname }}})

typedef struct {{{ prefix }}}_{{{ sname }}}_insert {
  isti_db *_db;
  isti_ins *_ins;
  ISTI_CORM_INSERTS_R({{{ prefix }}}_{{{ sname }}})
  {{ #fields }}
  {{{ prefix }}}_{{{ sname }}}_key_{{{ fname }}}_t *{{{ fname }}}_key;
  {{ /fields }}
} {{{ prefix }}}_{{{ sname }}}_insert;


// assemble everything into a single struct / namespace

typedef struct {{{ prefix }}}_{{{ sname }}}_fn {
  char *{{{ upper_sname }}};
  isti_cond_literal_t *table;
  {{{ prefix }}}_{{{ sname }}}_columns c;
  {{{ prefix }}}_{{{ sname }}}_select_alloc_t *select;
  {{{ prefix }}}_{{{ sname }}}_delete_alloc_t *delete;
  {{{ prefix }}}_{{{ sname }}}_insert_alloc_t *insert;
  {{{ prefix }}}_{{{ sname }}}_array_fn array;
  {{{ prefix }}}_{{{ sname }}}_free_t *free;
} {{{ prefix }}}_{{{ sname }}}_fn;

#define {{{ upper_prefix }}}_{{{ upper_sname }}}_AS(NAME_) static struct {{{ prefix }}}_{{{ sname }}}_fn NAME_ = { \\
  .{{{ upper_sname }}} = "\\"{{{ sname }}}\\"", \\
  {{ #fields }}
  .c.{{{ upper_fname }}} = "\\"{{{ fname }}}\\"", \\
  .c.{{{ upper_fname }}}_type = "{{{ sql_type }}}", \\
  ISTI_COND_PARAM_S(c, {{{ prefix }}}_{{{ sname }}}_column_{{{ fname }}}, {{{ fname }}}), \\
  ISTI_COND_PARAMS_S(c, {{{ prefix }}}_{{{ sname }}}_columns_{{{ fname }}}, {{{ fname }}}), \\
  .c.{{{ sname }}}_{{{ upper_fname }}} = "\\"{{{ sname }}}\\".\\"{{{ fname }}}\\"", \\
  ISTI_COND_PARAM_S(c, {{{ prefix }}}_{{{ sname }}}_column_{{{ sname }}}_{{{ fname }}}, {{{ sname }}}_{{{ fname }}}), \\
  ISTI_COND_PARAMS_S(c, {{{ prefix }}}_{{{ sname }}}_columns_{{{ sname }}}_{{{ fname }}}, {{{ sname }}}_{{{ fname }}}), \\
  {{ /fields }}
  .select = {{{ prefix }}}_{{{ sname }}}_select_alloc, \\
  .delete = {{{ prefix }}}_{{{ sname }}}_delete_alloc, \\
  .insert = {{{ prefix }}}_{{{ sname }}}_insert_alloc, \\
  ISTI_ARRAY_FNS_S(.array, {{{ prefix }}}_{{{ sname }}}_array), \\
  .free = {{{ prefix }}}_{{{ sname }}}_free \\
};
        ''', build_data(params, struct)), file=out)


def generate_c_preamble(out, **params):
    print(render('''
#include <stdio.h>

#include "isti.h"
#include "isti_flow.h"
#include "isti_sql.h"
#include "isti_str.h"

#include "{{{ header }}}"
    ''', build_data(params)), file=out)

def generate_c(struct, out, **params):
    print(render('''
// {{{ sname }}}

// mapping structs to and from the database

int {{{ prefix }}}_{{{ sname }}}_read_one(void *v, size_t n, char t, void *y) {
  {{{ sname }}} *x = ({{{ sname }}} *)v;
  switch (n) {
  {{ #fields }}
  case {{{ n }}}: x->{{{ fname }}} = {{ ^pointer }}*{{ /pointer }}({{{ type }}} *)y; break;
  {{ /fields }}
  default: return -1;
  }
  return 0;
}

int {{{ prefix }}}_{{{ sname }}}_read_any(void *v, size_t n, char t, void *y) {
  STATUS;
  {{{ prefix }}}_{{{ sname }}}_array *a = ({{{ prefix }}}_{{{ sname }}}_array *)v;
  {{{ sname }}} *x;
  if (n) {x = a->{{{ sname }}}[a->n.used-1];}
  else {
    ASSERT_MEM(x = calloc(1, sizeof(*x)));
    CHECK({{{ prefix }}}_{{{ sname }}}_array_inc(a, x));
  }
  CHECK({{{ prefix }}}_{{{ sname }}}_read_one(x, n, t, y));
  EXIT_STATUS;
}

int {{{ prefix }}}_{{{ sname }}}_free({{{ sname }}} *ptr, int previous) {
  STATUS;
  {{ #fields }}{{ #pointer }}if (ptr->{{{ fname }}}) free(ptr->{{{ fname }}});{{ /pointer }}{{ /fields }}
  free(ptr);
  RETURN_PREVIOUS;
}

int {{{ prefix }}}_{{{ sname }}}_free_data(void *data, size_t n, int previous) {
  STATUS;
  {{{ sname }}} **ptrs = ({{{ sname }}}**)data;
  for (size_t i = 0; i < n; ++i) {
    {{{ sname }}} *ptr = ptrs[i];
    CHECK({{{ prefix }}}_{{{ sname }}}_free(ptr, status));
  }
  free(data);
  EXIT_PREVIOUS;
}


// general table and array functions

ISTI_COND_LITERAL_C({{{ prefix }}}_{{{ sname }}}_table, "\\"{{{ sname }}}\\"")
ISTI_ARRAY_C({{{ prefix }}}_{{{ sname }}}_array, a, {{{ sname }}}*, {{{ sname }}}, {{{ prefix }}}_{{{ sname }}}_free_data)


// functions specific to select operations

// those that can be delegated to cond

ISTI_CORM_DELEGATE_LITERALS_C({{{ prefix }}}_{{{ sname }}}_select, {{{ prefix }}}_{{{ sname }}}_select)
{{ #fields }}
ISTI_COND_PARAM_C({{{ prefix }}}_{{{ sname }}}_column_{{{ fname }}}, "\\"{{{ fname }}}\\"", {{{ code }}}, {{{ type }}} {{ #pointer }}*{{ /pointer }})
static ISTI_CORM_DELEGATE_{{{ upper_code }}}_PARAM_C({{{ prefix }}}_{{{ sname }}}_select, {{{ prefix }}}_{{{ sname }}}_select_param_{{{ fname }}}, {{{ prefix }}}_{{{ sname }}}_column_{{{ fname }}})
ISTI_COND_PARAMS_C({{{ prefix }}}_{{{ sname }}}_columns_{{{ fname }}}, "\\"{{{ fname }}}\\"", {{{ code }}}, {{{ type }}} {{ #pointer }}*{{ /pointer }})
static ISTI_CORM_DELEGATE_{{{ upper_code }}}_PARAMS_C({{{ prefix }}}_{{{ sname }}}_select, {{{ prefix }}}_{{{ sname }}}_select_params_{{{ fname }}}, {{{ prefix }}}_{{{ sname }}}_columns_{{{ fname }}})
ISTI_COND_PARAM_C({{{ prefix }}}_{{{ sname }}}_column_{{{ sname }}}_{{{ fname }}}, "\\"{{{ sname }}}\\".\\"{{{ fname }}}\\"", {{{ code }}}, {{{ type }}} {{ #pointer }}*{{ /pointer }})
static ISTI_CORM_DELEGATE_{{{ upper_code }}}_PARAM_C({{{ prefix }}}_{{{ sname }}}_select, {{{ prefix }}}_{{{ sname }}}_select_param_{{{ sname }}}_{{{ fname }}}, {{{ prefix }}}_{{{ sname }}}_column_{{{ sname }}}_{{{ fname }}})
ISTI_COND_PARAMS_C({{{ prefix }}}_{{{ sname }}}_columns_{{{ sname }}}_{{{ fname }}}, "\\"{{{ sname }}}\\".\\"{{{ fname }}}\\"", {{{ code }}}, {{{ type }}} {{ #pointer }}*{{ /pointer }})
static ISTI_CORM_DELEGATE_{{{ upper_code }}}_PARAMS_C({{{ prefix }}}_{{{ sname }}}_select, {{{ prefix }}}_{{{ sname }}}_select_params_{{{ sname }}}_{{{ fname }}}, {{{ prefix }}}_{{{ sname }}}_columns_{{{ sname }}}_{{{ fname }}})
{{ /fields }}

// those with standard definitions

ISTI_CORM_SELECT_TEXT_C({{{ prefix }}}_{{{ sname }}})
ISTI_CORM_SELECT_ONE_C({{{ prefix }}}_{{{ sname }}}, {{{ sname }}}, {{ #fields }}{{{ code }}}{{ /fields }}, {{{ prefix }}}_{{{ sname }}}_read_one)
ISTI_CORM_SELECT_COUNT_C({{{ prefix }}}_{{{ sname }}})
ISTI_CORM_SELECT_ANY_C({{{ prefix }}}_{{{ sname }}}, {{{ prefix }}}_{{{ sname }}}_array, {{ #fields }}{{{ code }}}{{ /fields }}, {{{ prefix }}}_{{{ sname }}}_read_any)
ISTI_CORM_SELECT_FREE_C({{{ prefix }}}_{{{ sname }}})

// reset includes initial sql, so is explicit

static int {{{ prefix }}}_{{{ sname }}}_select_initial_sql({{{ prefix}}}_{{{ sname }}}_select *s) {
  STATUS;
  CHECK(s->_cond->selectn(s->_cond, {{ #fields }}"\\"{{{ sname }}}\\".\\"{{{ fname }}}\\"", {{ /fields }}NULL)->status);
  CHECK(s->_cond->from(s->_cond, "\\"{{{ sname }}}\\"")->status);
  EXIT_STATUS;
}

static int {{{ prefix }}}_{{{ sname }}}_select_reset({{{ prefix}}}_{{{ sname }}}_select *m) {
  STATUS;
  CHECK(isti_cond_reset(m->_cond));
  CHECK({{{ prefix }}}_{{{ sname }}}_select_initial_sql(m));
  EXIT_STATUS;
}

// expose select functionality in a struct

int {{{ prefix }}}_{{{ sname }}}_select_alloc({{{ prefix}}}_{{{ sname }}}_select **s, isti_db *db) {
  STATUS;
  ASSERT_MEM(*s = calloc(1, sizeof(**s)));
  (*s)->_db = db;
  {{ #fields }}
  (*s)->{{{ fname }}} = {{{ prefix }}}_{{{ sname }}}_select_param_{{{ fname }}};
  (*s)->{{{ fname }}}_ = {{{ prefix }}}_{{{ sname }}}_select_params_{{{ fname }}};
  (*s)->{{{ sname }}}_{{{ fname }}} = {{{ prefix }}}_{{{ sname }}}_select_param_{{{ sname }}}_{{{ fname }}};
  (*s)->{{{ sname }}}_{{{ fname }}}_ = {{{ prefix }}}_{{{ sname }}}_select_params_{{{ sname }}}_{{{ fname }}};
  {{ /fields }}
  ISTI_CORM_LITERALS_S((*s), {{{ prefix }}}_{{{ sname }}}_select)
  ISTI_CORM_SELECTS_S((**s), {{{ prefix }}}_{{{ sname }}})
  CHECK(isti_cond_alloc(&(*s)->_cond));
  CHECK({{{ prefix }}}_{{{ sname }}}_select_initial_sql(*s));
  EXIT_STATUS;
}


// functions specific to delete operations

// those that can be delegated to cond

ISTI_CORM_DELEGATE_LITERALS_C({{{ prefix }}}_{{{ sname }}}_delete, {{{ prefix }}}_{{{ sname }}}_delete)
{{ #fields }}
static ISTI_CORM_DELEGATE_{{{ upper_code }}}_PARAM_C({{{ prefix }}}_{{{ sname }}}_delete, {{{ prefix }}}_{{{ sname }}}_delete_param_{{{ fname }}}, {{{ prefix }}}_{{{ sname }}}_column_{{{ fname }}})
static ISTI_CORM_DELEGATE_{{{ upper_code }}}_PARAMS_C({{{ prefix }}}_{{{ sname }}}_delete, {{{ prefix }}}_{{{ sname }}}_delete_params_{{{ fname }}}, {{{ prefix }}}_{{{ sname }}}_columns_{{{ fname }}})
static ISTI_CORM_DELEGATE_{{{ upper_code }}}_PARAM_C({{{ prefix }}}_{{{ sname }}}_delete, {{{ prefix }}}_{{{ sname }}}_delete_param_{{{ sname }}}_{{{ fname }}}, {{{ prefix }}}_{{{ sname }}}_column_{{{ sname }}}_{{{ fname }}})
static ISTI_CORM_DELEGATE_{{{ upper_code }}}_PARAMS_C({{{ prefix }}}_{{{ sname }}}_delete, {{{ prefix }}}_{{{ sname }}}_delete_params_{{{ sname }}}_{{{ fname }}}, {{{ prefix }}}_{{{ sname }}}_columns_{{{ sname }}}_{{{ fname }}})
{{ /fields }}

// those with standard definitions

ISTI_CORM_DELETE_TEXT_C({{{ prefix }}}_{{{ sname }}})
ISTI_CORM_DELETE_GO_C({{{ prefix }}}_{{{ sname }}})
ISTI_CORM_DELETE_FREE_C({{{ prefix }}}_{{{ sname }}})

// reset includes initial sql, so is explicit

static int {{{ prefix }}}_{{{ sname }}}_delete_initial_sql({{{ prefix}}}_{{{ sname }}}_delete *s) {
  STATUS;
  CHECK(s->_cond->delete(s->_cond)->status);
  CHECK(s->_cond->from(s->_cond, "\\"{{{ sname }}}\\"")->status);
  EXIT_STATUS;
}

static int {{{ prefix }}}_{{{ sname }}}_delete_reset({{{ prefix}}}_{{{ sname }}}_delete *m) {
  STATUS;
  CHECK(isti_cond_reset(m->_cond));
  CHECK({{{ prefix }}}_{{{ sname }}}_delete_initial_sql(m));
  EXIT_STATUS;
}

// expose select functionality in a struct

int {{{ prefix }}}_{{{ sname }}}_delete_alloc({{{ prefix}}}_{{{ sname }}}_delete **s, isti_db *db) {
  STATUS;
  ASSERT_MEM(*s = calloc(1, sizeof(**s)));
  (*s)->_db = db;
  {{ #fields }}
  (*s)->{{{ fname }}} = {{{ prefix }}}_{{{ sname }}}_delete_param_{{{ fname }}};
  (*s)->{{{ fname }}}_ = {{{ prefix }}}_{{{ sname }}}_delete_params_{{{ fname }}};
  (*s)->{{{ sname }}}_{{{ fname }}} = {{{ prefix }}}_{{{ sname }}}_delete_param_{{{ sname }}}_{{{ fname }}};
  (*s)->{{{ sname }}}_{{{ fname }}}_ = {{{ prefix }}}_{{{ sname }}}_delete_params_{{{ sname }}}_{{{ fname }}};
  {{ /fields }}
  ISTI_CORM_LITERALS_S((*s), {{{ prefix }}}_{{{ sname }}}_delete)
  ISTI_CORM_DELETES_S((**s), {{{ prefix }}}_{{{ sname }}})
  CHECK(isti_cond_alloc(&(*s)->_cond));
  CHECK({{{ prefix }}}_{{{ sname }}}_delete_initial_sql(*s));
  EXIT_STATUS;
}


// functions specific to insert operations

// those that can be delegated to ins

{{ #fields }}
ISTI_INS_KEY_C({{{ prefix }}}_{{{ sname }}}_key_{{{ fname }}}, {{{ fname }}})
static ISTI_CORM_DELEGATE_KEY_C({{{ prefix }}}_{{{ sname }}}_insert, {{{ prefix }}}_{{{ sname }}}_insert_key_{{{ fname }}}, {{{ prefix }}}_{{{ sname }}}_key_{{{ fname }}})
{{ /fields }}

// those with standard definitions

ISTI_CORM_INSERT_FREE_C({{{ prefix }}}_{{{ sname }}})

// reset includes initial sql, so is explicit

static int {{{ prefix }}}_{{{ sname }}}_insert_initial_sql({{{ prefix}}}_{{{ sname }}}_insert *s) {
  STATUS;
  CHECK(s->_ins->table(s->_ins, "{{{ sname }}}")->status);
  {{ #fields }}
  CHECK(s->_ins->{{{ code }}}_column(s->_ins, "{{{ fname }}}")->status);
  {{ /fields }}
  EXIT_STATUS;
}

static int {{{ prefix }}}_{{{ sname }}}_insert_reset({{{ prefix}}}_{{{ sname }}}_insert *s) {
  STATUS;
  CHECK(isti_ins_reset(s->_ins));
  CHECK({{{ prefix }}}_{{{ sname }}}_insert_initial_sql(s));
  EXIT_STATUS;
}

// insert requires key handling for an arbitrary field, so is explicit

int {{{ prefix }}}_{{{ sname }}}_insert_one({{{ prefix }}}_{{{ sname }}}_insert *s, {{{ sname }}} *v) {
  STATUS;
  CHECK(s->_ins->status);
  isti_db *db = s->_db;
  CHECK(s->_ins{{ #fields }}->{{{ code }}}_value(s->_ins, v->{{{ fname }}}){{ /fields }}->status);
  if (s->_ins->_internal.key) {
    CHECK(db->sql_key(db, s->_ins->sql, s->_ins->_internal.key-1,
          {{{ prefix }}}_{{{ sname }}}_read_one, (void *)v));
  } else {
    CHECK(db->sql(db, s->_ins->sql));
  }
  EXIT_STATUS;
}

int {{{ prefix }}}_{{{ sname }}}_insert_any({{{ prefix }}}_{{{ sname }}}_insert *s, {{{ prefix }}}_{{{ sname }}}_array *a) {
  STATUS;
  CHECK(s->_ins->status);
  size_t key = s->_ins->_internal.key;
  for (size_t i = 0; i < a->n.used; ++i) { // either insert individuals or build sql
    {{{ sname }}} *v = a->{{{ sname }}}[i];
    if (key) {
      CHECK({{{ prefix }}}_{{{ sname }}}_insert_one(s, v));
      CHECK({{{ prefix }}}_{{{ sname }}}_insert_reset(s));
      s->_ins->_internal.key = key;
    } else {
      CHECK(s->_ins{{ #fields }}->{{{ code }}}_value(s->_ins, v->{{{ fname }}}){{ /fields }}->status);
    }
  }
  if (!key) { // execute built sql
    isti_db *db = s->_db;
    CHECK(db->sql(db, s->_ins->sql));
  }
  EXIT_STATUS;
}

// expose insert functionality in a struct

int {{{ prefix }}}_{{{ sname }}}_insert_alloc({{{ prefix}}}_{{{ sname }}}_insert **s, isti_db *db) {
  STATUS;
  ASSERT_MEM(*s = calloc(1, sizeof(**s)));
  (*s)->_db = db;
  {{ #fields }}
  (*s)->{{{ fname }}}_key = {{{ prefix }}}_{{{ sname }}}_insert_key_{{{ fname }}};
  {{ /fields }}
  ISTI_CORM_INSERTS_S((**s), {{{ prefix }}}_{{{ sname }}})
  CHECK(isti_ins_alloc(&(*s)->_ins));
  CHECK({{{ prefix }}}_{{{ sname }}}_insert_initial_sql(*s));
  EXIT_STATUS;
}

    ''', build_data(params, struct)), file=out)


def generate_sql(struct, out, **params):
    data = dict(params)
    data.update(struct)
    print(render('''
create table "{{{ sname }}}" (
{{ #fields }}  "{{{ fname }}}" {{{ sql_type }}}{{{ comma }}}
{{ /fields }});
    ''', data), file=out)
