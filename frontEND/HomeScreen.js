import React, { useState, useEffect } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, FlatList, Alert } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';
import { useNavigation } from '@react-navigation/native';

const HomeScreen = ({ route, navigation }) => {
  const [username, setUsername] = useState('');
  const [isDarkMode, setIsDarkMode] = useState(false);
  const { navigate } = useNavigation();

  useEffect(() => {
    if (route.params && route.params.username) {
      setUsername(route.params.username);
    }
  }, [route.params]);

  const handleLogout = async () => {
    console.log('Logout button clicked');
    try {
      const response = await fetch('http://10.0.2.2:5000/logout', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      Alert.alert('Logout Successful', data.message);
      navigate('Login');
    } catch (error) {
      console.error('Error during logout:', error);
      Alert.alert('Error', 'An error occurred during logout.');
    }
  };

  const handleAction = async (action) => {
    if (action === 'takeSurvey') {
      try {
        const response = await fetch('http://10.0.2.2:5000/survey', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Survey Data:', data);
        // Add logic to handle the received data, if needed
      } catch (error) {
        console.error('Error during API request:', error);
        // Add additional error handling if needed
      }
    } else if (action === 'surveyHistory') {
      // Add logic to navigate to the survey history screen
      console.log('Survey History pressed');
    }
  };

  const data = [
    { title: 'Take Survey', icon: 'ios-play', color: 'red', action: 'takeSurvey' },
    { title: 'Survey History', icon: 'ios-analytics', color: 'green', action: 'surveyHistory' },
  ];

  const renderItem = ({ item }) => (
    <TouchableOpacity
      style={[styles.button, { backgroundColor: item.color }]}
      onPress={() => handleAction(item.action)}
    >
      <Icon name={item.icon} size={40} color="white" />
      <Text style={styles.buttonText}>{item.title}</Text>
    </TouchableOpacity>
  );

  const toggleDarkMode = () => {
    setIsDarkMode((prevMode) => !prevMode);
    // Implement your logic to switch between light and dark mode here
  };

  return (
    <View style={[styles.container, isDarkMode && styles.darkModeContainer]}>
      <View style={styles.headerContainer}>
        <Text style={styles.headerText}>{`Hello, ${username}!`}</Text>
      </View>
      <FlatList
        data={data}
        renderItem={renderItem}
        keyExtractor={(item) => item.title}
        numColumns={2}
      />
      <TouchableOpacity
        style={[
          styles.toggleButton,
          { backgroundColor: isDarkMode ? 'black' : 'lightblue' },
        ]}
        onPress={toggleDarkMode}
      >
        <Icon
          name={isDarkMode ? 'ios-moon' : 'ios-sunny'}
          size={24}
          color={isDarkMode ? 'white' : 'yellow'}
        />
      </TouchableOpacity>
      <TouchableOpacity style={styles.logoutButton} onPress={handleLogout}>
        <Icon name="ios-exit" size={24} color="white" />
        <Text style={styles.logoutText}>Logout</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  // ... (styles definition remains the same)
  container: {
    flex: 1,
    backgroundColor: 'white',
  },
  darkModeContainer: {
    backgroundColor: '#333', // Adjust the color based on your dark mode preference
  },
  headerContainer: {
    padding: 20,
    borderBottomRightRadius: 50,
  },
  headerText: {
    fontSize: 24, // Increase font size for emphasis
    fontWeight: 'bold', // Apply bold style for a strong visual impact
    color: 'lightgrey', // Set text color to white
    textAlign: 'left', // Center-align the text
    textShadowColor: 'rgba(0, 0, 0, 0.75)', // Apply a subtle text shadow
    textShadowOffset: { width: 1, height: 1 }, // Adjust the shadow offset
    textShadowRadius: 2, // Set the shadow radius
  },
  button: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    margin: 10,
    borderRadius: 10,
    elevation: 2, // Add elevation for a shadow effect
  },
  buttonText: {
    marginTop: 8,
    fontSize: 16,
    color: 'white',
  },
  toggleButton: {
    position: 'absolute',
    bottom: 20,
    left: 20,
    flexDirection: 'row',
    alignItems: 'center',
    borderRadius: 10,
    padding: 10,
    elevation: 2, // Add elevation for a shadow effect
  },
  toggleButtonText: {
    marginLeft: 8,
    fontSize: 16,
    color: 'black', // Change the text color to match the login screen
  },
  logoutButton: {
    position: 'absolute',
    bottom: 20,
    right: 20,
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'red',
    borderRadius: 10,
    padding: 10,
    elevation: 2, // Add elevation for a shadow effect
  },
  logoutText: {
    marginLeft: 8,
    fontSize: 16,
    color: 'white',
  },
});

export default HomeScreen;
