Custom Date Format
When you import data into Zoho Analytics (from CSV, XLS, HTML etc., files) and if the data consists of date values, Zoho Analytics auto identifies the date column format based on the values provided. If there is any difference in the auto-identified date column format, the user could change it from the default list provided, or create a custom date format string that would match the date column. This document provides instructions on constructing a custom date format string.
Date Format Strings
The following table lists the supported strings to construct the date format.
| Format String | Meaning | Example |
| yy | Indicates Year value without century. If the value is from 70 to 99, year is assumed in 20th century (1970, 1971... 1999). Anything other than this is taken to be in the 21st century. | 79 (means 1979), 08 (means 2008), 14 (means 2014), 69 (means 2069). |
| yyyy | Indicates Year value with century | 2014 |
| MM | Indicates Month value in numeric | 3 (means March), 11 (means November) |
| MMM | Indicates Month value as a 3 letter string abbreviation (Jan, Feb) | Jan, Feb |
| MMMM | Indicates Month value in full string | January, February |
| dd | Indicates Day in the month | 12, 31 |
| EEE | Indicates Day in the week (abbreviation) | Wed, Sun |
| EEEE | Indicates Day in the week (full string form) | Wednesday, Sunday |
| HH | Indicates Time in 24-Hour format (0 to 23 hrs) | 13:50, 20:20 |
| hh | Indicates Time in 12-Hour format (0 to 12 hrs) (morning or afternoon is identified by AM or PM) | 1:30 AM, 11:30 PM |
| mm | Indicates Minutes in the hour | 1:30 |
| ss | Indicates Seconds in the minute | 11:30: 30 |
| SSS | Indicates the Millisecond in the Date | 11:30:30. 163 |
| a | Indicates AM/PM of the time | 11:00 AM, 2:00 PM |
| z | Indicates time zone based on either GMT or country specific time zones Note: On importing, the difference in time zone with respect to GMT will be altered accordingly and stored as GMT+00:00. To convert it to your time zone, use the Convert Time Zone function. | Nov 24, 2014 10:00 PM GMT+9:00 or Nov 24, 2014 10:00 PM JST will be saved in Zoho Analytics as Nov 24, 2014 01:00 PM GMT |
| Z | Indicates Time zone based RFC 822 standard To learn more about the working of this format, refer to the note in the above section. | Nov 24, 2014 +0900 Nov 24, 2014 -0247 |
| MILLI | Indicates number of milliseconds since January 1, 1970 | 911899079000 |
Separators
You can use any special characters (slash, comma, hyphen etc.,) as a separator for date. You can also use a different separator for each element. The following are a few examples of standard patterns.
- 24-11-2014
- 24.11.2014
- Nov 24 (Space is used as a separator)
- Nov 24, 2014 (Space and comma are used as separators)
- 24/11/2014 02:47 PM (Slash, colon and space are used as separators)
Examples:
The following table provides a few examples of different date format strings.
| Format | Examples |
| Date Only | |
| MM/dd | 11/24 |
| dd-MM | 24-11 |
| dd/MM/yy | 24/11/72 (72 means 1972. Click here to learn more.) |
| dd-MM-yy | 24-11-14 |
| dd.MM.yy | 24.11.14 |
| MM/dd/yyyy | 11/24/2014 |
| MM.dd.yyyy | 11.24.2014 |
| dd/MM/yyyy | 24/11/2014 |
| dd.MM.yyyy | 24.11.2014 |
| Date with Month Name | |
| dd MMM | 24 Nov |
| MMM-dd | Nov-24 |
| MMM-dd, yyyy | Nov-24, 2014 |
| MMM dd, yyyy | Nov 24, 2014 |
| dd MMM, yyyy | 24 Nov, 2014 |
| MMMM dd, yyyy | November 24, 2014 |
| dd MMMM, yyyy | 24 November, 2014 |
| Date with Day | |
| EEE, MMM dd yyyy | Wed, Nov 24, 2014 |
| dd-MM-yyyy, EEE | 24-11-2014, Wed |
| EEEE, MMM dd, yyyy | Wednesday, Nov 24, 2014 |
| dd/MM/yyyy, EEEE | 24/11/2014, Wednesday |
| Date with Time | |
| MM-dd, hh:mm:ss a | 11-24, 12:47:59 AM |
| MM-dd, HH:mm:ss | 11-24, 00:47:59 |
| MM/dd/yyyy hh:mm a | 11/24/2014 02:47 PM |
| MM/dd/yyyy HH:mm | 11/24/2014 14:47 |
| MM.dd.yyyy hh:mm a | 11.24.2014 02:47 PM |
| MM.dd.yyyy HH:mm | 11.24.2014 14:47 |
| Date with Month Name and Time | |
| dd MMM, yyyy hh:mm a | 24 Nov, 2014 02:47 PM |
| dd MMM, yyyy HH:mm | 24 Nov, 2014 14:47 |
| MMMM dd, yyyy hh:mm a | November 24, 2014 02:47 PM |
| MMMM dd, yyyy HH:mm | November 24, 2014 14:47 |
| EEEE, MMM dd, yyyy hh:mm a | Wednesday, Nov 24, 2014 02:47 PM |
| Time Zone | |
| dd MMM, yyyy hh:mm a z | 24 Nov, 2014 02:47 PM GMT+05.30 |
| MMMM dd, yyyy HH:mm Z | November 24, 2014 14:47 +0530 |
| To know about the working of time zone format strings, click here. |