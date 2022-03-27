import os
import time
import traceback

from registrationdata import db
from registrationdata.user import new_user, InvalidUserInfoError


def main():
    print("connecting to the database")
    tries = 10
    for i in range(tries):
        try:
            db.init()
        except Exception as e:
            if i == tries - 1:
                print(f"database connection attempt failed {tries} times", flush=True)
                return str(e)
        time.sleep(1)
    print("successfully connected to the database")

    try:
        total_added = 0
        retrying = False

        def abort():
            print(f"quitting (added {total_added} users in total)")

        while True:
            try:
                if retrying:
                    ans = input("\nwould you like to retry adding the user? [Y/n]: ")
                    retrying = False
                else:
                    ans = input("\nwould you like to register a new user? [Y/n]: ")
                if ans.casefold() == "n":
                    abort()
                    break
            except KeyboardInterrupt:
                abort()
                break

            try:
                usr = new_user()
                db.insert_user(usr)
            except InvalidUserInfoError as e:
                retrying = True
                print(e)
                continue
            except Exception:  # we being so damn lazy
                if os.environ['DO_TRACE'].casefold() == "yes":
                    traceback.print_exc()
                else:
                    print("internal server error, cannot record user stats")
                continue
            print(f"successfully recorded {usr.user_name} in the database")
    finally:
        db.close()
