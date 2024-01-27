import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button, TouchableOpacity, StyleSheet, Linking } from 'react-native';
import Icon from 'react-native-vector-icons/FontAwesome5';

const LoginScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [isDarkMode, setIsDarkMode] = useState(false);
  

  const handleLogin = async () => {
    try {
      const apiResponse = await fetch('http://10.0.2.2:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (!apiResponse.ok) {
        throw new Error(`HTTP error! Status: ${apiResponse.status}`);
      }

      const responseData = await apiResponse.json();

      if (responseData.message === 'Login successful') {
        if (responseData.id && responseData.username) {
          // Successful login with user data, navigate to the Home screen
          navigation.navigate('Home', { username: responseData.username });
        } else {
          // Successful login without user data, set an error to stay on the login page
          setError('Invalid response from the server. Please try again.');
        }
      } else if (responseData.message === 'Invalid username or password') {
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
  

  const handleGoogleSignIn = async () => {
    try {
      const apiResponse = await fetch('http://10.0.2.2:5000/google_login');
      const responseData = await apiResponse.json();
  
      if (responseData.url) {
        // Open the URL in the device's default web browser
        console.log(responseData.url);
        await Linking.openURL(responseData.url);
      } else {
        throw new Error('Invalid response from the server. URL not found.');
      }
    } catch (error) {
      console.error('Error during Google sign-in:', error);
      setError('An error occurred during Google sign-in. Please try again.');
    }
  };

  const toggleDarkMode = () => {
    // Toggle the dark mode state
    setIsDarkMode((prevMode) => !prevMode);
    // Implement your logic to switch between light and dark mode here
  };

  return (
    <View style={[styles.container, isDarkMode && styles.darkModeContainer]}>
      <View style={styles.box}>
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
        <View style={styles.buttonContainer}>
          <Button title="Login" onPress={handleLogin} />
          <Button title="Register" onPress={handleRegister} />
        </View>
        {error && <Text style={styles.error}>{error}</Text>}
        <TouchableOpacity
          style={styles.googleSignInButton}
          onPress={handleGoogleSignIn}
        >
          <Icon name="google" size={20} color="white" solid />
          <Text style={styles.googleSignInText}>Sign in with Google</Text>
        </TouchableOpacity>
      </View>
      <TouchableOpacity
        style={[styles.toggleButton, { backgroundColor: isDarkMode ? 'black' : 'lightblue' }]}
        onPress={toggleDarkMode}
      >
        <Icon name={isDarkMode ? 'moon' : 'sun'} size={20} style={isDarkMode ? styles.moonIcon : styles.sunIcon} solid />
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  darkModeContainer: {
    backgroundColor: '#333', // Adjust the color based on your dark mode preference
  },
  box: {
    width: '80%',
    padding: 20,
    backgroundColor: 'white',
    borderRadius: 10,
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    marginBottom: 16,
  },
  input: {
    width: '100%',
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 16,
    padding: 8,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '100%',
    marginBottom: 16,
  },
  error: {
    color: 'red',
    marginTop: 10,
  },
  toggleButton: {
    position: 'absolute',
    top: 10,
    right: 10,
    width: 40,
    height: 40,
    borderRadius: 10, // Make it a square button
    justifyContent: 'center',
    alignItems: 'center',
  },
  moonIcon: {
    color: 'white', // Make the moon icon white
  },
  sunIcon: {
    color: 'yellow', // Make the sun icon yellow
  },
  googleSignInButton: {
    marginTop: 20,
    backgroundColor: '#4285F4', // Google Blue
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 5,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
  },
  googleSignInText: {
    color: 'white',
    fontSize: 18,
    marginLeft: 10,
  },
});

export default LoginScreen;
