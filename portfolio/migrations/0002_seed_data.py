from django.db import migrations


def seed_data(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Tag = apps.get_model('portfolio', 'Tag')
    SkillCategory = apps.get_model('portfolio', 'SkillCategory')
    Project = apps.get_model('portfolio', 'Project')
    TimelineEntry = apps.get_model('portfolio', 'TimelineEntry')

    # --- Profile -------------------------------------------------------
    Profile.objects.get_or_create(pk=1, defaults=dict(
        name='Rukmini Kumari',
        role_title='Full-Stack Django Developer | Software Engineer',
        headline='Building products layer by **layer**.',
        intro=(
            "Full-stack developer with hands-on Django experience building "
            "authentication systems, REST APIs, and reusable application "
            "architecture across a marketplace, a recruitment platform, and a "
            "content platform. I've also self-initiated a Django starter "
            "framework now used as the base for new project builds, and solved "
            "200+ algorithmic problems on LeetCode in C++."
        ),
        about_heading=(
            "I like building things that go from a blank Django project to "
            "something a real user can log into."
        ),
        about_body=(
            "I'm a passionate Software Engineer and Full-Stack Django Developer "
            "focused on building scalable, secure, and user-centric web "
            "applications. I specialize in developing robust backend systems "
            "using Python, Django, REST APIs, and database technologies, while "
            "creating responsive and intuitive frontend experiences.\n\n"
            "I have a strong foundation in Data Structures and Algorithms using "
            "C++, and a deep interest in System Design — understanding scalable "
            "architectures, performance optimization, database design, caching "
            "strategies, and building systems that hold up under real-world "
            "load.\n\n"
            "Beyond the technical side, I take ownership of what I build, enjoy "
            "learning new technologies, and believe good software comes out of "
            "collaboration — sharing knowledge, communicating clearly, and "
            "working toward a shared goal as a team."
        ),
        phone='8355030900',
        github_url='https://github.com/rukmini12438',
        linkedin_url='https://www.linkedin.com/in/rukmini-96b005287',
        leetcode_url='https://leetcode.com/u/Rukmini2025',
        grad_year='2027',
        leetcode_count='200+',
        profile_photo='profile/rukmini_profile.jpg',
        resume_file='resume/rukmini_resume.pdf',
    ))

    # --- Tags (shared between skills + project chips) ------------------
    tag_names = [
        # Backend & Frameworks
        'Django', 'Django REST Framework', 'REST API Design', 'Django ORM',
        'django-allauth', 'Authentication Systems',
        # Frontend
        'HTML5', 'CSS3', 'JavaScript', 'Bootstrap 5',
        # Databases, Tools & Languages
        'SQLite', 'MySQL', 'Git', 'GitHub', 'VS Code', 'Postman',
        'C', 'C++', 'Python',
        # System Design & DSA
        'Scalable Architecture', 'Performance Optimization', 'Database Design',
        'Caching Strategies', 'Load Balancing', 'High-Level Design (HLD)',
        'Low-Level Design (LLD)', 'Data Structures & Algorithms',
    ]
    tags = {}
    for n in tag_names:
        tags[n], _ = Tag.objects.get_or_create(name=n)

    # --- Skill categories -----------------------------------------------
    backend, _ = SkillCategory.objects.get_or_create(
        name='Backend & Frameworks', defaults=dict(order=1)
    )
    backend.skills.set([
        tags['Django'], tags['Django REST Framework'], tags['REST API Design'],
        tags['Django ORM'], tags['django-allauth'], tags['Authentication Systems'],
    ])

    frontend, _ = SkillCategory.objects.get_or_create(
        name='Frontend & Web Technologies', defaults=dict(order=2)
    )
    frontend.skills.set([tags['HTML5'], tags['CSS3'], tags['JavaScript'], tags['Bootstrap 5']])

    data_tools, _ = SkillCategory.objects.get_or_create(
        name='Databases, Tools & Languages', defaults=dict(order=3)
    )
    data_tools.skills.set([
        tags['SQLite'], tags['MySQL'], tags['Git'], tags['GitHub'],
        tags['VS Code'], tags['Postman'], tags['C'], tags['C++'], tags['Python'],
    ])

    system_design, _ = SkillCategory.objects.get_or_create(
        name='System Design & DSA', defaults=dict(
            order=4,
            description=(
                "200+ problems solved on LeetCode in C++, with a deep interest "
                "in how large systems are actually put together — scalable "
                "architecture, performance optimization, database design, "
                "caching, and load balancing."
            ),
        )
    )
    system_design.skills.set([
        tags['Data Structures & Algorithms'], tags['Scalable Architecture'],
        tags['High-Level Design (HLD)'], tags['Low-Level Design (LLD)'],
        tags['Database Design'], tags['Caching Strategies'], tags['Load Balancing'],
        tags['Performance Optimization'],
    ])

    # --- Projects --------------------------------------------------------
    p1, _ = Project.objects.get_or_create(
        slug='securehire-ai',
        defaults=dict(
            title='SecureHire AI',
            order=1,
            status='live',
            short_description=(
                "An AI-assisted recruitment platform built as a modular, "
                "multi-app Django project. I architected a scalable app "
                "structure that separates concerns across candidate, job, and "
                "evaluation modules, so each part of the hiring workflow can be "
                "developed and tested independently — a pattern I carried over "
                "from the reusable Django starter framework I built for myself."
            ),
        )
    )
    p1.tags.set([tags['Django'], tags['Python'], tags['HTML5'], tags['CSS3'],
                 tags['Bootstrap 5'], tags['SQLite']])

    p2, _ = Project.objects.get_or_create(
        slug='localfix',
        defaults=dict(
            title='LocalFix',
            order=2,
            status='live',
            short_description=(
                "A full-stack local services marketplace connecting users with "
                "nearby service providers. Booking and review modules are built "
                "on Django's app-based modular architecture, and the platform "
                "is accessibility-first by design: callback requests, OTP-based "
                "phone signup, and an icon-first UI so non-literate users can "
                "navigate it without relying on text."
            ),
        )
    )
    p2.tags.set([tags['Django'], tags['HTML5'], tags['CSS3'], tags['Bootstrap 5'], tags['SQLite']])

    p3, _ = Project.objects.get_or_create(
        slug='cookly',
        defaults=dict(
            title='Cookly',
            order=3,
            status='live',
            short_description=(
                "A full-stack recipe web app built with Django, Bootstrap 5, "
                "and SQLite, following Django's MVT architecture end to end — "
                "models, views, and templates all designed from scratch to "
                "serve bilingual recipe content across four categories."
            ),
        )
    )
    p3.tags.set([tags['Django'], tags['Bootstrap 5'], tags['SQLite']])

    # --- Timeline ----------------------------------------------------------
    TimelineEntry.objects.get_or_create(
        title='B.Tech, Computer Science & IT',
        defaults=dict(
            date_label='2023 — 2027',
            description=(
                'Ajay Kumar Garg Engineering College, Ghaziabad. Coursework in '
                'DBMS, OOP, and core CS fundamentals alongside independent '
                'full-stack project work.'
            ),
            order=1,
        )
    )
    TimelineEntry.objects.get_or_create(
        title='Built a reusable Django starter framework',
        defaults=dict(
            date_label='Ongoing',
            description=(
                'Self-initiated a Django project template covering '
                'authentication (login, signup, password reset) and modular '
                'app architecture — now the base I build every new project on.'
            ),
            order=2,
        )
    )
    TimelineEntry.objects.get_or_create(
        title='Independent Django project builds',
        defaults=dict(
            date_label='Ongoing',
            description=(
                'SecureHire AI, LocalFix, and Cookly — three complete '
                'applications built and documented end-to-end, module by '
                'module.'
            ),
            order=3,
        )
    )
    TimelineEntry.objects.get_or_create(
        title='Competitive programming & system design',
        defaults=dict(
            date_label='Ongoing',
            description=(
                '200+ problems solved on LeetCode in C++, alongside continued '
                'study of scalable architecture, caching, and database design.'
            ),
            order=4,
        )
    )


def unseed_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
