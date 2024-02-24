import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:login/login_page.dart';

void main() {
  testWidgets('Login page UI test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(MaterialApp(home: LoginPage()));

    // Verify that the login page UI is displayed correctly.
    expect(find.text('Login'), findsOneWidget);
    expect(find.text('Username'), findsOneWidget);
    expect(find.text('Password'), findsOneWidget);
    expect(find.byType(ElevatedButton), findsOneWidget);

    // Verify that the increment button is disabled initially.
    expect(tester.widget<ElevatedButton>(find.byType(ElevatedButton)).enabled, false);

    // Enter a valid username and password.
    await tester.enterText(find.byKey(const Key('username_field')), 'testuser');
    await tester.enterText(find.byKey(const Key('password_field')), 'password');

    // Verify that the increment button is enabled after entering text.
    expect(tester.widget<ElevatedButton>(find.byType(ElevatedButton)).enabled, true);

    // Tap the login button.
    await tester.tap(find.byType(ElevatedButton));
    await tester.pump();

    // Verify that the login action is triggered.
    // You may add additional verification logic based on your login implementation.
    expect(find.text('Welcome to the Dashboard!'), findsOneWidget);
  });
}
