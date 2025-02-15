get_user_pass = "SELECT name, password,isAdmin FROM USERS WHERE name=:username "

create_user = "INSERT INTO USERS (name, password, isAdmin) VALUES (:username, :password, :isAdmin)"