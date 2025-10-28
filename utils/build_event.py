from icalendar import Calendar, Event
import pytz
from datetime import datetime, timedelta


def build_event_duration(summary: str, description: str, start: datetime, duration: int, location: str,
                         freq_of_recurrence: str, until: datetime) -> Event:
    r"""
    Return an event that can be added to a calendar
    Args:
        summary: title/summary of the event
        description: description of the event
        start: datetime.datetime object of the event start time
        duration: duration in hours
        location: location of the event
        freq_of_recurrence: daily, weekly, monthly
        until: datetime.datetime object of when recurrence ends

    Returns:
        icalendar.Event object
    """

    event = Event()
    event.add('summary', summary)
    event.add('description', description)
    event.add('dtstart', start)
    event.add('duration', timedelta(hours=duration))
    event.add('dtstamp', datetime.now())
    event.add('location', location)
    event.add('rrule', {'FREQ': freq_of_recurrence, 'UNTIL': until})

    return event


# Converts time to datetime object for India/Asia/Kolkata timezone
def generate_india_time(year: int, month: int, date: int, hour: int, minutes: int):
    """
    Create a timezone-aware datetime in Asia/Kolkata.
    Note: Use tz.localize to avoid incorrect LMT offsets from assigning tzinfo directly.
    """
    tz = pytz.timezone('Asia/Kolkata')
    naive = datetime(year, month, date, hour, minutes)
    return tz.localize(naive)
