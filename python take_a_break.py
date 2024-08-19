import time  #provides various time
from plyer import notification #module is used to create and display desktop notifications.


def notify_break():  #function is defined to send a notification.
  notification.notify(
        title = "Time to Take a Break!", #The title of the notification
      #The body of the notification, reminding the user to take a break
        message = "You've been working for a while. Take a break for 5-10 minutes.",
      #duration (in seconds) for which the notification is displayed
        timeout = 5

    )


if __name__ == "__main__": #This condition ensures that the code within it runs only if the script is executed directly,
    while True: #This creates an infinite loop,
        app_icon="" # enter app icone.
        notify_break() #function to display the notification.
        time.sleep( 60 * 60)  # Notification every 1 hour (3600 seconds)#This ensures that the notification is shown every hour.

