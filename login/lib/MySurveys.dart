import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Survey Questions',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: SurveyPage(),
    );
  }
}

class SurveyPage extends StatefulWidget {
  @override
  _SurveyPageState createState() => _SurveyPageState();
}

class _SurveyPageState extends State<SurveyPage> {
  List<Map<String, dynamic>> questions = [
    {'question': 'How satisfied are you with our service?', 'answer': null},
    {'question': 'Would you recommend our product to others?', 'answer': null},
    // Add more questions as needed
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Survey Questions'),
      ),
      body: ListView.builder(
        itemCount: questions.length,
        itemBuilder: (context, index) {
          return Card(
            margin: EdgeInsets.symmetric(horizontal: 10, vertical: 5),
            child: Padding(
              padding: EdgeInsets.all(10),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Question ${index + 1}: ${questions[index]['question']}',
                    style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                  ),
                  SizedBox(height: 10),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                      ElevatedButton(
                        onPressed: () {
                          setState(() {
                            questions[index]['answer'] = 'Very Satisfied';
                          });
                        },
                        child: Text('Very Satisfied'),
                      ),
                      ElevatedButton(
                        onPressed: () {
                          setState(() {
                            questions[index]['answer'] = 'Satisfied';
                          });
                        },
                        child: Text('Satisfied'),
                      ),
                      ElevatedButton(
                        onPressed: () {
                          setState(() {
                            questions[index]['answer'] = 'Neutral';
                          });
                        },
                        child: Text('Neutral'),
                      ),
                      ElevatedButton(
                        onPressed: () {
                          setState(() {
                            questions[index]['answer'] = 'Dissatisfied';
                          });
                        },
                        child: Text('Dissatisfied'),
                      ),
                      ElevatedButton(
                        onPressed: () {
                          setState(() {
                            questions[index]['answer'] = 'Very Dissatisfied';
                          });
                        },
                        child: Text('Very Dissatisfied'),
                      ),
                    ],
                  ),
                  SizedBox(height: 10),
                  if (questions[index]['answer'] != null)
                    Text(
                      'Your answer: ${questions[index]['answer']}',
                      style: TextStyle(fontWeight: FontWeight.bold),
                    ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
