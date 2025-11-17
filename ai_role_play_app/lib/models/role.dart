class Role {
  final String id;
  final String name;
  final String icon;
  final String description;
  final String prompt;
  final String greeting;

  Role({
    required this.id,
    required this.name,
    required this.icon,
    required this.description,
    required this.prompt,
    required this.greeting,
  });

  factory Role.fromJson(Map<String, dynamic> json) {
    return Role(
      id: json['id'] as String,
      name: json['name'] as String,
      icon: json['icon'] as String,
      description: json['description'] as String,
      prompt: json['prompt'] as String,
      greeting: json['greeting'] as String,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'icon': icon,
      'description': description,
      'prompt': prompt,
      'greeting': greeting,
    };
  }
}
