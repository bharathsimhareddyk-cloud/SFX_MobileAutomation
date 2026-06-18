# import smtplib
# import shutil
# from email.message import EmailMessage
#
# # Zip the Allure report
# shutil.make_archive("allure-report", "zip", "allure-report")
#
# EMAIL = "bharathsimhareddy.k@shadowfax.in"
# PASSWORD = "132G1a0220@"      # Replace with your actual password or use environment variables
# TO_EMAIL = "bharathsimhareddy.k@shadowfax.in"
#
# msg = EmailMessage()
# msg["Subject"] = "Automation Test Report"
# msg["From"] = EMAIL
# msg["To"] = TO_EMAIL
#
# msg.set_content("Please find the attached Allure report.")
#
# with open("allure-report.zip", "rb") as f:
#     msg.add_attachment(
#         f.read(),
#         maintype="application",
#         subtype="zip",
#         filename="allure-report.zip"
#     )
#
# with smtplib.SMTP("smtp.office365.com", 587) as smtp:
#     smtp.starttls()
#     smtp.login(EMAIL, PASSWORD)
#     smtp.send_message(msg)
#
# print("✅ Report sent successfully")