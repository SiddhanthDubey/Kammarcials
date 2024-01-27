// RegisterScreen.js
import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, TouchableOpacity } from 'react-native';
import Icon from 'react-native-vector-icons/FontAwesome5'; // Import the FontAwesome5 icons

const RegisterScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [mobile, setMobile] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const handleRegister = async () => {
    try {
      // Check for null or empty values
      if (!username || !mobile || !password) {
        setError('Please fill in all fields.');
        return;
      }

      const apiUrl = 'http://10.0.2.2:5000/register'; // Update with your actual Flask API URL

      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, mobile, password }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const responseData = await response.json();

      if (responseData.success) {
        navigation.navigate('Login');
      } else {
        // Handle unsuccessful registration
        setError(responseData.message || 'Registration failed. Please try again.');
      }
    } catch (error) {
      console.error('Error during registration:', error);
      setError('An error occurred. Please try again.');
    }
  };

  const handleBackToLogin = () => {
    // Navigate back to the Login screen
    navigation.navigate('Login');
  };

  const toggleDarkMode = () => {
    // Toggle the dark mode state
    setIsDarkMode((prevMode) => !prevMode);
    // Implement your logic to switch between light and dark mode here
  };

  return (
    <View style={[styles.container, isDarkMode && styles.darkModeContainer]}>
      <TouchableOpacity
        style={[
          styles.toggleButton,
          isDarkMode
            ? [styles.darkModeToggleButton, { backgroundColor: 'black' }]
            : [styles.lightModeToggleButton, { backgroundColor: 'lightblue' }],
        ]}
        onPress={toggleDarkMode}
      >
        {/* Use the FontAwesome5 icons based on the dark mode state */}
        <Icon
          name={isDarkMode ? 'moon' : 'sun'}
          size={20}
          color={isDarkMode ? 'white' : 'yellow'}
          solid
        />
      </TouchableOpacity>
      <View
        style={[
          styles.squareContainer,
          isDarkMode && styles.darkModeSquare,
        ]}
      >
        <Text style={styles.title}>Register</Text>
        <TextInput
          style={styles.input}
          placeholder="Username"
          value={username}
          onChangeText={setUsername}
        />
        <TextInput
          style={styles.input}
          placeholder="Mobile"
          value={mobile}
          onChangeText={setMobile}
        />
        <TextInput
          style={styles.input}
          placeholder="Password"
          secureTextEntry
          value={password}
          onChangeText={setPassword}
        />
        <View style={styles.buttonContainer}>
          <Button title="Register" onPress={handleRegister} />
          <Button title="Back to Login" onPress={handleBackToLogin} />
        </View>
        {error && <Text style={styles.error}>{error}</Text>}
      </View>
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
  squareContainer: {
    width: '80%',
    padding: 20,
    backgroundColor: 'white', // Background color of the square in light mode
    borderRadius: 10,
    alignItems: 'center',
  },
  darkModeSquare: {
    backgroundColor: 'white', // Background color of the square in dark mode
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
    borderRadius: 10,
    padding: 10,
  },
  toggleButtonText: {
    color: 'white',
  },
  lightModeToggleButton: {
    borderRadius: 10, // Make the button a square
  },
  darkModeToggleButton: {
    borderRadius: 10, // Make the button a perfect circle
  },
});

export default RegisterScreen;
