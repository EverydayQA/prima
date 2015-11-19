
#ifndef ISTI_FLOW_H_
#define ISTI_FLOW_H_

#include "isti_log.h"
#include "isti.h"

/// @file
/// @brief Macros that abstract program flow.
///
/// These are used internally by the library.  Clients do not need to
/// use them (but are welcome to do so, if they want).
///
/// They  assume that a `status` variable has been defined with @ref STATUS
/// and that an exit label is available via @ref EXIT.  All code assumes
/// that zero (false) status is success.

/// The status is defined as ISTI_OK on entry;
#define STATUS int status = ISTI_OK
/// Return values from calls are checked and, on error, we jump to exit;
#define CHECK(EXPR) do {if ((status = (EXPR))) goto exit;} while(0)
/// Errors can be 'raised' explicitly
#define FAIL_SILENT(CODE) status = CODE; goto exit
#define FAIL(CODE, ...) ISTI_LOG(__VA_ARGS__); FAIL_SILENT(CODE)
/// Assertions and allocs are checked;
#define ASSERT_SILENT(EXPR, CODE) do {if (!(EXPR)) {FAIL_SILENT(CODE);}} while(0)
#define ASSERT(EXPR, CODE, ...) do {if (!(EXPR)) {FAIL(CODE, __VA_ARGS__);}} while(0)
#define ASSERT_MEM(EXPR) ASSERT(EXPR, ISTI_ERR_MEM, "Out of memory\n")
/// Functions have a final exit point;
#define EXIT exit:
/// After which we return status
#define RETURN return status
/// Often we return immediately
#define EXIT_STATUS EXIT RETURN
/// Clean-up functions (eg free) don't overwrite earlier errors.
#define RETURN_PREVIOUS return previous ? previous : status
/// Clean-up functions (eg free) don't overwrite earlier errors.
#define EXIT_PREVIOUS EXIT RETURN_PREVIOUS
/// Merge status result
#define CLEANUP(OPERATION) {int _status = OPERATION; status = status ? status : _status;}

#endif
