// LoginScreen.js
import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const LoginScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const handleLogin = async () => {
    try {
      const apiUrl = 'http://10.0.2.2:5000/login'; // Update with your actual Flask API URL
      
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const responseData = await response.json();

      if (responseData.success) {
        // Successful login, navigate to the next screen
        navigation.navigate('Home'); // Change 'Home' to your desired screen name
      } else {
        // Handle unsuccessful login
        setError(responseData.message || 'Login failed. Please check your credentials.');
      }
    } catch (error) {
      console.error('Error during login:', error);
      setError('An error occurred. Please try again.');
    }
  };

  const handleRegister = () => {
    // Navigate to the Register screen
    navigation.navigate('Register');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Login</Text>
      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <Button title="Login" onPress={handleLogin} />
      <Button title="Register" onPress={handleRegister} />
      {error && <Text style={styles.error}>{error}</Text>}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    marginBottom: 16,
  },
  input: {
    width: '80%',
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 16,
    padding: 8,
  },
  error: {
    color: 'red',
    marginTop: 10,
  },
});

export default LoginScreen;
