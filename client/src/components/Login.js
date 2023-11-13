import React, { useState } from "react";


function Login({setUser, user}) {
    const [loginEmail, setLoginEmail] = useState("");
    const [loginPwd, setLoginPass] = useState("");
    const [newEmail, setNewEmail] = useState("");
    const [newPwd, setNewPass] = useState("");

    function handleLogin(e) {
        e.preventDefault();

        const data = {
            email: loginEmail,
            passowrd: loginPwd
        };

        fetch(), {}
    }
}