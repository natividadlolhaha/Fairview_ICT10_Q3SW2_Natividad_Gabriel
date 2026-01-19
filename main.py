from pyscript import document
def intramsteam(event=None):
    registration = document.getElementById("registration").value
    medical = document.getElementById("medicalclearance").value
    section = document.getElementById("section").value
    gradelevel = document.getElementById("gradelevel").value

    if registration == "no1" and medical == "no2":             # checks if you have registered or have medical clearance, if you have then no problem if not it displays message saying to register and get medical clearance
        message = (
            "Kindly register online before proceeding.<br>"
            "Kindly secure medical clearance from the clinic.")

    elif registration == "no1":                                # same function as previous except if only one of them is not met ex: registered but no medical clearance
        message = "Kindly register online before proceeding."
    elif medical == "no2":
        message = "Kindly secure medical clearance from the clinic."
    elif gradelevel == "7" or gradelevel == "8" or gradelevel == "9" or gradelevel == "10":     # checks grade level. if its above grade 11 it displays message saying not eligible
        
        if section == "Ruby":
            team = "Green Hornets"
            image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJAwBKBzgqq-Dit6GeklRWqCahxvBFAXZ89A&s'
        elif section == "Sapphire":
            team = "Yellow Tigers"
            image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFtLbS-bbYiXTQOscGaflhDc459sN3olDdgA&s'
        elif section == "Topaz":
            team = "Blue Bears"
            image = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/2010-kodiak-bear-1.jpg/1280px-2010-kodiak-bear-1.jpg'
        elif section == "Emerald":
            team = "Red Bulldogs"
            image = 'https://media.istockphoto.com/id/620408634/photo/stretching-of-english-bulldog.jpg?s=612x612&w=0&k=20&c=73FPZossvVgxRssbSL8YtumSC4qN8ai7cu-T_o0-zTM='
        else:
            team = "Unassigned Team"
        message = f"Congratulations! You are part of the <strong>{team}</strong>."
        message += f"<img src='{image}' style='max-width: 220px; margin-top: 15px;'>"
    else:
        message = "Only students from Grades 7 to 10 are eligible for Intramurals."
    document.getElementById("result").innerHTML = message
document.getElementById("button").onclick = intramsteam
