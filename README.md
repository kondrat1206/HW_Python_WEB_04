# Send Message Application

This is a WEB application.

## Installation:

1. Clone the repository:

   ```bash
   git clone https://github.com/kondrat1206/HW_Python_WEB_04.git
   ```

   ```bash
   cd ./HW_Python_WEB_04
   ```



2. Run the application with docker:

   - Build docker image

   ```bash
   docker build . -t messages
   ```
   
   - Start image container

   ```bash
   docker run -v C:\messages\storage:/messages/storage -p 3000:3000 messages
   ```



## Usage:

1. Connect to your Host mashine with browser and link: http://ip_addr_your_host_mashine:3000/

2. Select "Send message" link.

3. Send your message.

The Message with Username will be saved to the file "data.json" in the C:\messages\storage directory of your host mashine.

PROFIT!!!
