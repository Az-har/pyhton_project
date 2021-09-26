import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("azharayyash1000@gmail.com", "ayyash12345")
server.sendmail(
  "azharayyash1000@gmail.com", 
  "azharayyash999@gmail.com", 
  "this message is from python")
server.quit()