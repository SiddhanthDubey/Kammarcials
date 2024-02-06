import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:myapp/LoginPage.dart';

class RegisterPage extends StatefulWidget {
  const RegisterPage({Key? key}) : super(key: key);

  @override
  State<RegisterPage> createState() => _RegisterPageState();
}

class _RegisterPageState extends State<RegisterPage> {
  final TextEditingController usernameController = TextEditingController();
  final TextEditingController mobileController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  Future<void> _register() async {
    try {
      final String apiUrl =
          "http://10.0.2.2:5000/register"; // Replace with your Flask backend URL

      final Map<String, dynamic> data = {
        "username": usernameController.text,
        "mobile": mobileController.text,
        "password": passwordController.text,
      };

      final http.Response response = await http.post(
        Uri.parse(apiUrl),
        headers: {
          "Content-Type": "application/json",
        },
        body: json.encode(data),
      );
      print(data);

      if (response.statusCode == 201) {
        // Successful registration, navigate to login page
        print("Registration Successful");
        print(response.body);

        // Navigate to login page
        Navigator.pushReplacement(
            context, MaterialPageRoute(builder: (context) => LoginPage()));
      } else {
        // Handle registration failure
        print("Registration Failed");
        print(response.body);
      }
    } catch (e) {
      // Log and handle the error
      print("Error during registration: $e");
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Register screen'),
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text(
              'Register',
              style: TextStyle(
                fontSize: 35,
                color: Colors.blue,
                fontWeight: FontWeight.bold,
              ),
            ),
            Form(
              child: Column(
                children: [
                  TextFormField(
                    controller: usernameController,
                    decoration: InputDecoration(
                      labelText: 'Username',
                      hintText: 'Enter Username',
                      prefixIcon: Icon(Icons.person),
                      border: OutlineInputBorder(),
                    ),
                  ),
                  SizedBox(
                    height: 20,
                  ),
                  TextFormField(
                    controller: mobileController,
                    keyboardType: TextInputType.emailAddress,
                    decoration: InputDecoration(
                      labelText: 'Mobile',
                      hintText: 'Enter Mobile',
                      prefixIcon: Icon(Icons.email),
                      border: OutlineInputBorder(),
                    ),
                  ),
                  SizedBox(
                    height: 20,
                  ),
                  TextFormField(
                    controller: passwordController,
                    keyboardType: TextInputType.visiblePassword,
                    decoration: InputDecoration(
                      labelText: 'Password',
                      hintText: 'Enter Password',
                      prefixIcon: Icon(Icons.password),
                      border: OutlineInputBorder(),
                    ),
                    obscureText: true,
                  ),
                  SizedBox(
                    height: 30,
                  ),
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 50),
                    child: MaterialButton(
                      minWidth: double.infinity,
                      onPressed: _register,
                      child: Text('Register'),
                      color: Colors.blue,
                      textColor: Colors.white,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
