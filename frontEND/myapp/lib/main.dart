import 'package:flutter/material.dart';
import 'package:myapp/Dashboard.dart';
import 'package:myapp/LoginPage.dart';
import 'package:myapp/Register.dart'; // Assuming your RegisterPage file is named RegisterPage.dart

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(primarySwatch: Colors.deepPurple),
      initialRoute: '/login', // Set initial route to '/login'
      routes: {
        '/login': (context) => LoginPage(),
        '/register': (context) =>
            RegisterPage(), // Add a route for the RegisterPage
        '/dashboard': (context) => MyHomePage(),
      },
    );
  }
}
