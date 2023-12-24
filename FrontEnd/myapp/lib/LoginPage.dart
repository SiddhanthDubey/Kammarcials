import 'package:flutter/material.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
    home: Scaffold(
      appBar: AppBar(
        title: Text('Login screen'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Text(
            'Login',
            style: TextStyle(
              fontSize: 35,
              color: Colors.teal,
              fontWeight: FontWeight.bold
            ),
          
          ),
          Form(
            child: Column(
              children: [

                TextFormField(
                  keyboardType: TextInputType.emailAddress,
                  decoration: InputDecoration(
                    labelText: 'Email',
                    hintText: 'Enter Email',
                    prefixIcon: Icon(Icons.email),
                    border: OutlineInputBorder(),
                  ),
                  onChanged: (String value){

                  },
                  validator: (value){
                    return value!.isEmpty? 'Please enter Email':null;
                  },
                ),
                SizedBox(height:30,),
                TextFormField(
                  keyboardType: TextInputType.visiblePassword,
                  decoration: InputDecoration(
                    labelText: 'Password',
                    hintText: 'Enter Password',
                    prefixIcon: Icon(Icons.password),
                    border: OutlineInputBorder(),
                  ),
                  onChanged: (String value){

                  },
                  validator: (value){
                    return value!.isEmpty? 'Please enter Password':null;
                  },
                ),
                SizedBox(height:30,),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 50),
                  child: MaterialButton(
                  minWidth: double.infinity,  
                  onPressed: () {},
                  child: Text('Login'),
                  color: Colors.teal,
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