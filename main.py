from pyscript import document

def check_team(event=None):
    registration = document.getElementById("registration").value
    medical = document.getElementById("medicalclearance").value
    section = document.getElementById("section").value

    # Priority checks
    if registration == "no1" and medical == "no2":
        message = (
            "❌ Kindly register online before proceeding.<br>"
            "❌ Kindly secure medical clearance from the clinic."
        )

    elif registration == "no1":
        message = "❌ Kindly register online before proceeding."

    elif medical == "no2":
        message = "❌ Kindly secure medical clearance from the clinic."

    else:
        # Team assignment
        if section == "Ruby":
            team = "Green Hornets"
        elif section == "Sapphire":
            team = "Yellow Tigers"
        elif section == "Topaz":
            team = "Blue Bears"
        elif section == "Emerald":
            team = "Red Bulldogs"
        else:
            team = "Unassigned Team"

        message = f"✅ You are {section}."