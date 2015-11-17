
#ifndef ISTI_H_
#define ISTI_H_

/** @mainpage

## Introduction

This is an experimental and incomplete C library, exploring a variety
of ideas:

- stylised error handling with macros;
- namespacing;
- a lack of ADTs (transparent data structures);
- struct-relational mapping (ORM for C);
- auto-generation of C code from Python.

You could call this an "opinionated" library, because it tries to
follow various ideas to their logical conclusion.  But I'm not so
keen on that term, because I'm not so certain that the ideas are good.
So this library is partly an experiment in seeing how useful certain
ideas can be.

Because of this "opinionated" nature, it may take some time to
understand what the code is doing.  The rest of this document is
intended as a very rapid introduction to the various ideas.

## Error Handling

The minimum that the external user needs to know is that non-zero
(true) return values indicate an error.  These codes are defined
in @ref isti_flow.h.

But if you read any of the implementation code then you will
benefit from understanding that:

- almost every function returns an integer status;
- the internal status is called `status` and is defined via the
  @ref STATUS macro;
- almost every function has a label for cleanup and exit, called
  `exit:` and defined via the @ref EXIT macro;
- almost every function call is checked;
- checking for internal status values is performed with the
  @ref CHECK macro;
- checking for boolean values (true; eg malloc success) is
  performed with the @ref ASSERT macro.

None of these macros are complex.  They are used simply to
encourage uniform, consistent handling of status values.

## Namespacing

Most header files define a library, implemented in the similarly
named source file.  Libraries are defined as structs, named via
macros.  This gives a form of namespacing.  For example:

@code
ISTI_MEM_AS(mem)

int isti_str_allow(isti_str *s, char *chars) {
  STATUS;
  ASSERT(s->c = mem.extend(s->c, strlen(chars)+1, sizeof(*s->c), &s->n),
         ISTI_ERR_MEM);
  EXIT_STATUS;
}
@endcode

(The error handling in this code is described above.)

Here the library defined in @ref isti_mem.h is introduced into the
`mem` namespace (struct).  The function `mem.extend` is equivalent
to the function @ref isti_mem_extend.

## Transparent data structures

It's standard practice for "good quality" C libraries to "hide" implementation
details, exposing only `void*` pointers as Abstract Data Types (see, for
example, Hanson's C Interfaces and Implementations).  However, many other
languages (particularly Python) take a different approach, exposing the
information while trusting the user to use it carefully.

This latter approach is sometimes called "lightweight" because, with less
information hidden, less functionality needs to be provided by the library -
you can use existing tools to manipulate exposed data.

In this library, data structures are generally visible.  So, for example,
you can access the `char*` contents of a string directly (@ref isti_str).
And you are expected to do so.  But (obviously?) you should not *change* the
value unless you are *very* sure that you know what you are doing.

*/

/// @file
/// @brief Main header for ISTI clib

/// Intentionally false to support inline checks.
#define ISTI_OK 0

/// Typically, failure on alloc.
#define ISTI_ERR_MEM 1 
/// Poorly formatted SQL command, etc.
#define ISTI_ERR_SQL 2
/// Error calling sqlite
#define ISTI_ERR_SQLITE 3
/// Error inside ORM code
#define ISTI_ERR_CORM 4
/// Error inside string code
#define ISTI_ERR_STR 5
/// Error calling ODBC
#define ISTI_ERR_ODBC 6

/// Cannot find a result in a query
#define ISTI_ERR_NO_RESULT 100


/// Warning - multiple evaluation.
#define ISTI_MIN(a, b) ((a) < (b) ? (a) : (b))
/// Warning - multiple evaluation.
#define ISTI_MAX(a, b) ((a) > (b) ? (a) : (b))

#endif
