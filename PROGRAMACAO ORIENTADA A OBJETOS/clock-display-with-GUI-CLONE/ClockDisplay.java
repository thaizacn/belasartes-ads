
/**
 * The ClockDisplay class implements a digital clock display for a
 * European-style 24 hour clock. The clock shows hours and minutes. The 
 * range of the clock is 00:00 (midnight) to 23:59 (one minute before 
 * midnight).
 * 
 * The clock display receives "ticks" (via the timeTick method) every minute
 * and reacts by incrementing the display. This is done in the usual clock
 * fashion: the hour increments when the minutes roll over to zero.
 * 
 * @author Michael Kölling and David J. Barnes
 * @version 2016.02.29
 */
public class ClockDisplay
{
    private NumberDisplay days;
    private NumberDisplay months;
    private NumberDisplay years;
    private NumberDisplay hours;
    private NumberDisplay minutes;
    private String displayString;    // simulates the actual display
    
    /**
     * Constructor for ClockDisplay objects. This constructor 
     * creates a new clock set at 00:00.
     */
    public ClockDisplay()
    {
        days = new NumberDisplay(31);
        months = new NumberDisplay(12);
        years = new NumberDisplay(1000);
        hours = new NumberDisplay(24);
        minutes = new NumberDisplay(60);
        updateDisplay();
    }

    /**
     * Constructor for ClockDisplay objects. This constructor
     * creates a new clock set at the time specified by the 
     * parameters.
     */
    public ClockDisplay(int day, int month, int year, int hour, int minute)
    {
        days = new NumberDisplay(31);
        months = new NumberDisplay(12);
        years = new NumberDisplay(1000);
        hours = new NumberDisplay(24);
        minutes = new NumberDisplay(60);
        setTime(day, month, year, hour, minute);
    }

    /**
     * This method should get called once every minute - it makes
     * the clock display go one minute forward.
     */
    public void timeTick()
    {
        minutes.increment();
        if (minutes.getValue() == 0) {  // minutes rolled over to zero
            hours.increment();
            if (hours.getValue() == 0) {  // hours rolled over to zero
                days.increment();
                if (days.getValue() == 0) {  // days rolled over to one
                    months.increment();
                    if (months.getValue() == 0) {  // months rolled over to one
                        years.increment();
                    }
                }
            }
        }
        updateDisplay();
    }

    /**
     * Set the time of the display to the specified hour and
     * minute.
     */
    public void setTime(int day, int month, int year, int hour, int minute)
    {
        days.setValue(day);
        months.setValue(month);
        years.setValue(year);
        hours.setValue(hour);
        minutes.setValue(minute);
        updateDisplay();
    }

    /**
     * Return the current time of this display in the format DD-MM-YY HH:MM.
     */
    public String getTime()
    {
        return displayString;
    }
    
    /**
     * Update the internal string that represents the display.
     */
    private void updateDisplay()
    {
        displayString = String.format("%02d-%02d-%02d %02d:%02d",
                                      days.getValue(),
                                      months.getValue(),
                                      years.getValue(),
                                      hours.getValue(),
                                      minutes.getValue());
    }
}