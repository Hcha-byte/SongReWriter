# Error Codes and Subtypes Reference

This table provides a structured list of error categories, their primary codes, and subtypes to allow for more precise error handling.

| Category                  | Primary Code | Subtype                | Description                                               |
|---------------------------|--------------|------------------------|-----------------------------------------------------------|
| **Success**               | 0            | `SUCCESS`              | Operation completed successfully.                         |
| **File Errors**           | 1            | `FILE_NOT_FOUND`       | The specified file does not exist.                        |
|                           |              | `FILE_READ_ERROR`      | Unable to read the file due to permissions or corruption. |
|                           |              | `FILE_WRITE_ERROR`     | Unable to write to the file.                              |
|                           |              | `EMPTY_FILE`           | The file exists but contains no data.                     |
| **Input Errors**          | 2            | `INVALID_ARGUMENT`     | The provided argument is not valid.                       |
|                           |              | `MISSING_ARGUMENT`     | A required argument was not provided.                     |
|                           |              | `OUT_OF_RANGE`         | A numeric or indexed value is outside the expected range. |
| **Network Errors**        | 3            | `CONNECTION_FAILED`    | Failed to establish a connection to a server.             |
|                           |              | `TIMEOUT`              | The network request took too long to respond.             |
|                           |              | `HOST_UNREACHABLE`     | The target host is not reachable.                         |
| **System Errors**         | 4            | `MEMORY_ALLOCATION`    | The system could not allocate the required memory.        |
|                           |              | `RESOURCE_EXHAUSTED`   | A system resource has been depleted.                      |
|                           |              | `UNSUPPORTED_PLATFORM` | The operation is not supported on the current OS.         |
| **Parsing Errors**        | 5            | `INVALID_FORMAT`       | The input format does not match the expected structure.   |
|                           |              | `MALFORMED_JSON`       | The JSON data is incorrectly formatted.                   |
|                           |              | `ENCODING_ERROR`       | Encoding or decoding operation failed.                    |
| **Database Errors**       | 6            | `CONNECTION_LOST`      | Lost connection to the database server.                   |
|                           |              | `QUERY_FAILED`         | The database query could not be executed.                 |
|                           |              | `DATA_INTEGRITY`       | Data violates constraints or expected consistency.        |
| **Authentication Errors** | 7            | `INVALID_CREDENTIALS`  | Username or password is incorrect.                        |
|                           |              | `UNAUTHORIZED_ACCESS`  | User lacks the necessary permissions.                     |
|                           |              | `TOKEN_EXPIRED`        | The authentication token is no longer valid.              |
| **Hardware Errors**       | 8            | `DISK_FAILURE`         | A hardware disk error occurred.                           |
|                           |              | `OVERHEAT_WARNING`     | The system temperature exceeds safe limits.               |
|                           |              | `DEVICE_NOT_FOUND`     | The requested hardware device is not available.           |
| **General Errors**        | 9            | `UNKNOWN_ERROR`        | An unexpected error occurred.                             |
|                           |              | `OPERATION_ABORTED`    | The operation was canceled before completion.             |
|                           |              | `UNSPECIFIED_FAILURE`  | Failure without a specific category.                      |

## Usage Recommendations

- Use **primary codes** for broad categorization.
- Use **subtypes** to provide more specific error context.
- Log both the **primary code** and **subtype** for better debugging.

