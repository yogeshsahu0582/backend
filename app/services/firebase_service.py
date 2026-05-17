import firebase_admin

from firebase_admin import credentials
from firebase_admin import messaging

from firebase_admin.exceptions import FirebaseError

cred = credentials.Certificate(
    "firebase/serviceAccountKey.json"
)

if not firebase_admin._apps:

    firebase_admin.initialize_app(cred)

def send_push_notification(
    token: str,
    title: str,
    body: str
):

    try:

        message = messaging.Message(

            notification=messaging.Notification(
                title=title,
                body=body
            ),

            token=token
        )

        response = messaging.send(message)

        return {
            "success": True,
            "response": response
        }

    except FirebaseError as e:

        return {
            "success": False,
            "error": str(e)
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }