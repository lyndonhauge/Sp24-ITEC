csharp = input('Have you taken the C# programming class? Type "yes" if so: ')
java = input('Have you taken the Java programming class? Type "yes" if so: ')

# or statement checks if a user has entered it for either one of them.
if csharp == 'yes' or java == 'yes':
    print('You can take iOS programming!')
else:
    print('You need to take either C# or Java')
