"""add jobs

Revision ID: 30529347fd00
Revises: 5f1277d2b383
Create Date: 2025-02-07 10:51:19.260057

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30529347fd00'
down_revision: Union[str, None] = '5f1277d2b383'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        INSERT INTO public.jobs (company_id, title, experience_level, location, date_of_listing, description)
VALUES 
    (28, 'Marketing Coordinator', 'Marketing (1 year preferred), Graphic Design (2 years preferred)', 'Princeton, NJ', CURRENT_DATE, 'A leading real estate firm in New Jersey is seeking an administrative Marketing Coordinator with some experience in graphic design. You will be working closely with our fun, kind, ambitious members of the sales team and our dynamic executive team on a daily basis. This is an opportunity to be part of a fast-growing, highly respected real estate brokerage with a reputation for exceptional marketing and extraordinary culture of cooperation and inclusion. You must be a well-organized, creative, proactive, positive, and most importantly, kind-hearted person. Please, be responsible, respectful, and cool-under-pressure. Please, be proficient in Adobe Creative Cloud (Indesign, Illustrator, Photoshop) and Microsoft Office Suite. Above all, have fantastic taste and be a good-hearted, fun-loving person who loves working with people and is eager to learn. Our office is a fast-paced environment. You will work directly with a Marketing team and communicate daily with other core staff and our large team of agents. This description is a brief overview, but your skills and interests will be considered in what you work on and as the role evolves over time. Agent Assistance - Receive & Organize Marketing Requests from Agents. Track Tasks & Communicate with Marketing team & Agents on Status - Prepare print materials and signs for open houses- Submit Orders to Printers & Communicate & Track Deadlines Graphic Design & Branding - Managing brand strategy and messaging through website, social media, videos, online advertising, print placement and events. Receive, organize, and prioritize marketing requests from agents. Fulfill agent design requests including postcards, signs, email marketing and property brochures using pre-existing templates and creating custom designs. Maintain brand assets and generic files. Events & Community - Plan and execute events and promotions, Manage Contacts & Vendors for Event Planning & Sponsorships. Our company is committed to creating a diverse environment and is proud to be an equal opportunity employer. All qualified applicants will receive consideration for employment without regard to race, color, religion, gender, gender identity or expression, sexual orientation, national origin, genetics, disability, age, or veteran status. Pay: $18-20/hour. Expected hours: 35 to 45 per week. Benefits: Paid time off. Schedule: 8 hour shift, Monday to Friday.'),
	(29, 'Assistant Restaurant Manager', 'Prefer 1 to 3 years FOH management experience.', 'Cincinnati, OH', CURRENT_DATE, 'The National Exemplar is accepting applications for an Assistant Restaurant Manager. We offer highly competitive wages, healthcare, paid time off, complimentary dining privileges and bonus opportunities. We are a serious, professional, long-standing neighborhood restaurant with over 41 years of service. If you are looking for a long-term fit with a best in class organization then you should apply now. Please send a resumes to pardom@nationalexemplar.com. Candidate should be a self-starter, proactive, attentive to details and like developing others. Must have a strong sense of teamwork and strong witten and verbal communication skills. Have a keen interest in service, food and learning. Passion for excellence and doing things right.'),
	(30, 'Senior Elder Law / Trusts and Estates Associate Attorney', '10-15 years of experience, Experience with various advance directives, trusts, and wills.', 'New Hyde Park, NY', CURRENT_DATE, 'Senior Associate Attorney - Elder Law / Trusts and Estates. Our legal team is committed to providing each client with quality counsel, innovative solutions, and personalized service. Founded in 2000, the firm offers the legal expertise of its 115+ attorneys, who have accumulated experience and problem-solving skills over decades of practice. We are a prominent Lake Success Law Firm seeking an associate attorney for its growing Elder Law and Estate Planning practice. The successful candidate will be a self-motivated, detail-oriented team member with strong communication skills and a desire to grow their practice. Experience with Estate Planning, Administration, and Litigation and is preferred. Responsibilities will include: Counseling clients with regard to estate planning and asset protection; Formulating and overseeing execution of Medicaid and estate plans;Drafting wills, revocable and irrevocable trusts, powers of attorney, health care proxies, and living wills; Estate Administration; Trust Administration; Court Appearances for Estate and Proceedings; Supervising paralegals. 
Qualifications: Juris Doctor degree (J.D.) from an accredited law school. Licensed to practice law in New York. Strong analytical and problem-solving skills. Ability to build rapport with clients. Excellent written and verbal communication skills. Competitive salary commensurate with experience. Salary: $140,000- $175,000. Benefits: 401k, Medical, Dental, Life Insurance, PTO, and more. This position is based out of Lake Success, NY. This position requires a baseline understanding of online marketing including Search Engine Marketing, Search Engine Optimization, and campaign analytics. The ideal candidate must be an analytical and detailed dynamic, self-starter who is proactive, and able to multitask effectively. This individual must be a strategic thinker with excellent verbal and written communication, as well strong presentation skills and the ability to work independently in an organized manner.'),
	(31, 'Economic Development and Planning Intern', NULL, 'Raleigh, NC', CURRENT_DATE, 'Job Summary:
The Economic Development and Planning Intern will provide valuable support to the Economic Development and Planning team, with a specific focus on urban planning and transportation initiatives during the upcoming summer semester. This role is ideal for a local graduate or undergraduate student with a keen interest in economic development, city planning, and a passion for contributing to the growth of a vibrant downtown community.

Responsibilities and Essential Functions:
- Support the Planning and Transportation Manager and the Economic Development and Planning team in major planning and advocacy initiatives, such as the ongoing Downtown Economic Development Strategy.
- Assist in coordination efforts related to transportation planning and major downtown projects such as Raleigh''s first Bus Rapid Transit line.
- Contribute to the creation of reports, including the annual State of Downtown and quarterly market reports.
- Assist in data collection, analysis, and maintenance of downtown data.
- Support small business and retail recruitment programs.
- Participate in stakeholder meetings and community engagement efforts.

Qualifications:
- Currently enrolled in a graduate or undergraduate program with a focus on urban planning, economics, business, research, public administration, geography, sustainability, or a related field.
- Strong interest in economic development, city planning, and community revitalization.
- Excellent analytical and research skills, with a keen eye for detail.
- Proficiency in Microsoft Office Suite and data analysis tools.
- Effective communication skills, both written and verbal.

Benefits:
- Gain hands-on experience in economic development and city planning.
- Work closely with a dynamic and experienced team of economic development and planning professionals.
- Networking opportunities with local stakeholders and professionals.
- Compensation for your contributions.

Physical Requirements:
- Prolonged periods sitting at a desk and working on a computer.
- Must be able to lift up to 15 pounds at times.
- Must be able to access various departments of a given location.

Position Environment:
This is an in-person role, with the candidate reporting to the Downtown Raleigh Alliance offices at 333 Fayetteville Street, Suite 1150, Raleigh, NC. Office space will be provided onsite at DRA, and the intern may also be in the field providing support to the Downtown Raleigh community. DRA will provide parking for regular or required on-site work and will also offer the option of transit passes for regular or on-site work. Travel outside of periodic travel to and from Downtown Raleigh and the DRA office will not be required for this position.

Other Duties:
Please note this job description is not designed to cover or contain a comprehensive listing of activities, duties, or responsibilities that are required of the employee for this job. Duties, responsibilities, and activities may change at any time with or without notice.

Compensation:
This is a temporary, part-time position, approximately 12 to 20 hours a week, limited to a maximum 14-week term, aligned with the summer university calendar. The anticipated pay range is $14 - $20 an hour, commensurate with qualifications and prior experience. This position is non-exempt and not eligible for benefits at DRA.

How to Apply:
Please submit your resume and cover letter highlighting your interest in economic development and planning to marysell@downtownraleigh.org. Applications will be accepted until Monday, May 6. Interviews will be scheduled on a rolling basis.

EEO Statement:
We are an equal employment opportunity employer and do not discriminate against any person based on race, color, creed, religion, national origin, political affiliation, sex, gender identity or expression, sexual orientation, age, disability, genetic information, or other reasons prohibited by law. This nondiscrimination and opportunity policy extends to employment, use of all company facilities, membership, board service and leadership, volunteerism, participation in any of the organization''s programs or services, and all employment actions such as promotions, compensation, benefits, and termination of employment.
'),
	(32, 'Producer', NULL, 'United States', CURRENT_DATE, 'Company Description

Raw Cereal is a creative design agency specializing in live, interactive, corporate, and installation-based entertainment. Our mission is to push boundaries and create unique and immersive experiences for our clients. We pride ourselves on our end-to-end creative services and cutting-edge use of technology for larger-than-life productions.

Role Description

We''re looking for Directors, Producers, Creatives, AI Programmers, 3D Artists, Senior Motion Graphics Artists, Editors, etc. If you think you have something to add, please reach out.

Email: Jobs@rawcereal.com'),
	(33, 'Respiratory Therapist', 'Minimum one year of experience in respiratory therapy (Preferred), Experience working with pediatric patients (Preferred)', 'Omaha, NE', CURRENT_DATE, 'Company Description

Children''s is the region''s only full-service pediatric healthcare center, where our people make us the very best for kids. Come cultivate your passion, purpose, and professional development in an environment of excellence and inclusion, where team members are supported and deeply valued. Opportunities for career growth abound as we expand our services and spaces, including the cutting-edge Hubbard Center for Children. Join our highly engaged, caring team and help us provide brighter, healthier tomorrows for the children we serve. Children''s is committed to diversity and inclusion. We are an equal opportunity employer, including veterans and people with disabilities.

A Brief Overview

Provides appropriate respiratory care specific to the pediatric population in accordance with hospital policies and procedures. Assesses, plans, and implements appropriate respiratory care based on the cardiopulmonary needs of patients. Evaluates the effectiveness of care plans and recommends revisions to the multidisciplinary team.

Essential Functions

- Set up and operate devices such as mechanical ventilators, therapeutic gas administration apparatus, environmental control systems, and aerosol generators, following specified treatment parameters.
- Determine treatment requirements, including type, methods, and duration of therapy, precautions to be taken, and medication dosages, compatible with physician orders.
- Read physician orders, measure arterial blood gases, and review patient information to assess conditions.
- Explain treatment procedures to patients to gain cooperation and alleviate concerns.
- Monitor patient physiological responses to therapy, such as vital signs, arterial blood gases, and blood chemistry changes, consulting with physicians if adverse reactions occur.
- Administer therapeutic gases, including nitrogen, nitric oxide, and heliox.
- Enforce safety rules and ensure careful adherence to physician orders.
- Maintain charts containing patient identification and therapy information.
- Inspect, clean, test, and maintain respiratory therapy equipment to ensure safe and efficient operation, notifying supervisors when repairs are necessary.
- Educate patients and families about conditions and teach appropriate disease management techniques such as breathing exercises and the use of respiratory medications and equipment.
- Perform broncho-pulmonary drainage and assist or instruct patients in breathing exercises.
- Conduct lung capacity tests to evaluate cardiopulmonary functions.
- Provide emergency care, including artificial respiration, external cardiac massage, and assistance with cardiopulmonary resuscitation.
- Complete all required respiratory therapy competency tests within specified timelines.
- Demonstrate competency in identified technical skills for the respiratory department.

Clinical Instructor Responsibilities (if applicable)

- Supervise respiratory therapy students in the clinical hospital setting.
- Orient students to their role, including scope of service, policies and procedures, patient safety, and professionalism.
- Introduce students to the equipment used by respiratory therapists at Children''s.
- Provide supervised hands-on learning in a clinical setting.
- Ensure accurate documentation of all respiratory therapy performed with students.
- Ensure accurate handoff of patient information and ordered respiratory therapy.

Education Qualifications

- Graduate of an accredited AMA-approved school of respiratory care accredited by the National Board of Respiratory Care (Required)
- Bachelor''s degree from an AMA-approved accredited school in respiratory care (Preferred)

Skills and Abilities

- Demonstrated competency in technical skills related to the Respiratory Therapy department.

Licenses and Certifications

- Licensed Respiratory Care Practitioner (Current and valid Nebraska license required)
- Basic Life Support (BLS) through the American Heart Association (Required)
- Registered Respiratory Therapist (RRT) credential within one year (Required)
- Neonatal/Pediatric Respiratory Therapist (RRT-NPS) credential within three years of hire (Required)
- Pediatric Advanced Life Support (PALS) within 180 days (Required)

Children''s is the very best for kids—and the very best for your career! At Children''s, we put YOU first so together, we can improve the life of every child.'),
	(34, 'Worship Leader', 'At least two years of experience in general office responsibilities and procedures, and two years of experience in graphic design and media.', 'Palm Bay, FL', CURRENT_DATE, 'We''re excited about the future of our church, and we''re looking for a passionate and energetic leader to help us make disciples for Jesus in Palm Bay, Florida, and beyond.

What We''re Looking For: The ideal candidate will lead our worship team to craft meaningful and inspiring musical worship for our Sunday gatherings. You’ll also shepherd the team, helping them grow in their faith and discipleship. This position is for someone ready to invest in the life of our church family and take ownership of the worship ministry to help it thrive and move forward.

Key Skills:

    A vibrant, growing relationship with Jesus Christ
    A strong commitment to the vision, mission, and leadership standards of our church
    Ability to lead worship musicians in creating excellent, authentic modern worship (e.g., Hillsong, Elevation)
    Exceptional vocal and/or instrumental talent
    Proficiency with Multitracks, Planning Center Online, and ProPresenter (or a willingness to learn quickly)

Responsibilities:

    Lead worship for Sunday morning gatherings
    Conduct rehearsals to prepare for Sundays
    Other duties as assigned

Additional Information:

    Local connections for team building are a plus
    This is a part-time position to start, with the potential to increase hours as the church grows
    Hours per week: Less than 10

How to Apply:
When you apply, please include a link to a video of you leading worship in a service setting.

Job Description:

Knowledge, Skills, and Abilities:

    Proficient in Microsoft Office; ability to learn ProPresenter and online applications like Google Calendar and Planning Center. Familiarity with Photoshop and Adobe Premiere is a plus.
    Strong writing, analytical, and problem-solving skills.
    Familiar with social networking applications such as Facebook and Twitter.
    Ability to communicate clearly, both verbally and in writing.
    Skilled in operating standard office equipment, such as computers, telephones, copiers, and fax machines.
    Ability to follow both oral and written instructions.
    Strong follow-up skills with excellent attention to detail.
    Basic graphic design and video editing skills are a huge plus, but not required.

Minimum Qualifications:
    Proficiency in computer usage, including internet and word processing.
    Knowledge of basic office management and organizational practices.
    Ability to work independently or as part of a team.
    Must be fully committed to the mission of FBC Melbourne/Bay West Church.'),
	(35, 'Inside Customer Service Associate', 'Experience in a business sales environment or college coursework in business and marketing is a plus. Previous customer service experience required.', 'Saginaw, MI', CURRENT_DATE, 'Glastender Inc. is a family-owned manufacturer of top-quality commercial bar and restaurant equipment, providing innovative solutions to the industry for over 50 years. We''re dedicated to delivering exceptional customer experiences and are currently seeking an Inside Customer Service Associate to join our team.

Key Responsibilities:

    Communicate with customers to provide outstanding service, addressing inquiries, orders, and product information via phone and email.
    Design bar equipment layouts using Glastender products to meet customer needs.
    Compile and submit quotations, verify orders, enter orders into the system, and create detailed shop drawings for production.
    Maintain up-to-date product knowledge and stay informed on industry trends to support customer needs effectively.
    Keep customer records updated in the system.
    Multi-task across various software programs efficiently, with proficiency in word processing, spreadsheets, and AutoCAD (preferred).

Qualifications:

    Strong communication, organizational, and attention-to-detail skills.
    Strong computer skills and ability to manage multiple software programs.
    Ability to thrive in a collaborative, team-oriented environment.

If you''re passionate about delivering exceptional customer service and enjoy supporting a dynamic sales team, we''d love to hear from you. Join Glastender Inc. and be part of an industry leader that values excellence in everything we do.'),
	(35, 'Production Supervisor', 'A college degree or 5-7 years of related work experience.', 'Saginaw, MI', CURRENT_DATE, 'Glastender Inc. is seeking a Production Supervisor with strong leadership and organizational skills to manage our production team and processes. This role requires the ability to meet specific production targets and efficiently manage resources.

Key Responsibilities:

    Lead and organize a team to achieve production goals.
    Apply lean manufacturing principles to improve production efficiency.
    Communicate effectively with team members and other departments.
    Provide training and presentations to staff as needed.

Qualifications:

    Strong understanding of lean manufacturing principles.
    Excellent communication, organizational, and presentation skills.
    Proficiency with computers and various software programs.

If you''re an experienced leader who thrives in a fast-paced, team-driven environment, this is an excellent opportunity to join Glastender Inc. and help shape the future of our production processes.'),
	(36, 'Project Architect', 'Bachelor’s or Master’s degree in Architecture from an accredited institution. 5-10 years of experience working in an architectural firm.', 'St Louis, MO', CURRENT_DATE, 'PGAV Destinations is looking for a self-motivated and highly creative individual with a solid understanding of architectural technical aspects. The ideal candidate should be quick to learn, collaborative, and possess a strong work ethic, with the ability to manage multiple projects simultaneously. You will play an integral role in coordinating complex, design-intensive projects, guiding less experienced teammates along the way. The role will involve all stages of design, from concept to construction documentation and administration.

Key Skills:

    Strong hand and digital sketching abilities.
    Proficiency in Revit, AutoCAD, and Microsoft Office Suite.
    Proficiency in Adobe Creative Suite.
    Familiarity with 3D modeling software such as Rhino, SketchUp, and/or 3ds Max (preferred).
    Excellent verbal and written communication skills.
    Knowledge of building codes, including ADA, and the ability to perform code analysis.
    In-depth understanding of architectural building systems.

Job Requirements:

    Ability to travel as needed.
    Effective communication with the project team and clients.
    Strong coordination skills with consultants.
    Ability to work independently and problem-solve without constant guidance.
    Licensure is preferred, but not required.
    Construction Administration or on-site experience is a plus, but not required.
    Ability to lead small and large-scale projects from concept design through construction administration, in collaboration with a Project Manager or Senior Project Architect.

How to Apply:
Please send your resume, portfolio, and a one-page cover letter (maximum 9 MB file size) to venita.davidson@pgav.com.'),
	(37, 'Senior Product Marketing Manager', 'Minimum of 7 years of experience in pharmaceutical product marketing, with a proven track record of success. Experience in immunology, and preferably gastroenterology.', 'United States', CURRENT_DATE, 'A leading pharmaceutical company, dedicated to developing and commercializing innovative, high-quality medicines that improve patient lives, is seeking a Senior Product Marketing Manager. This role will be responsible for creating and executing marketing strategies for one or more pharmaceutical products. The ideal candidate will work closely with cross-functional teams—such as sales, medical affairs, market research, and commercial operations—to develop and implement integrated marketing plans that drive product awareness, adoption, and revenue growth.

Key Responsibilities:

    Develop and execute integrated marketing plans for pharmaceutical products.
    Serve as the Marketing point of contact for patient support initiatives, including patient HUBs, advocacy groups, and bridge programs.
    Utilize customer insights and market analysis to inform marketing strategies and create tactical plans.
    Collaborate with cross-functional teams to design and implement product-specific promotional campaigns across various channels, such as digital, print, and events.
    Manage product-specific budgets and track performance against marketing objectives and KPIs.
    Participate in product launch planning and ensure the effective execution of launch activities.
    Work with the Training team to identify training needs and develop sales force training materials.

Requirements:

    Strong knowledge of the pharmaceutical industry, including regulatory requirements, product development, and commercialization.
    Excellent communication and interpersonal skills, with the ability to collaborate effectively across teams.
    Strong analytical skills with the ability to use market research data to shape marketing strategies.
    Ability to manage budgets and track marketing performance.
    Self-motivated, with the ability to work both independently and as part of a team.
    Willingness to travel up to 20%.'),
	(38, 'Osteogenic Loading Coach', 'Customer service: 1 year (preferred). Health, fitness, or medical: 1 year (preferred)', 'Anchorage, AK', CURRENT_DATE, 'OsteoStrong® is a unique wellness center focused on strengthening the skeletal system, which is the foundation of the body. Unlike a gym, diet, or medical treatment, OsteoStrong® offers a proven strategy to improve bone density, posture, balance, athletic performance, and reduce joint and back pain. We work with individuals of all ages, helping them strengthen their bones using a method called Osteogenic Loading, which delivers measurable results quickly.

We are looking for a passionate coach to join our team! Our focus is primarily on women over 50, helping them rebuild lost bone density so they can age with strength and grace. As one of the fastest-growing wellness franchises, we are committed to helping people live healthier, more fulfilling lives. This is a fantastic opportunity to be part of a team that truly empowers others. Plus, you’ll enjoy three-day weekends almost every week, as we are open Monday through Thursday and offer flexible hours.

Key Responsibilities:

    Instruct and coach members on our four osteogenic loading devices, which help increase bone density, reduce fracture risks, and improve strength, stamina, and balance.
    Educate clients on proper form and technique (we will train you!).
    Assist members with "Bio Hack" therapies, including red light therapy, PEMI (pulsed electromagnetic induction therapy), compression boots, hydromassage, and vibration therapy.
    Create a friendly, supportive environment where members feel motivated and valued.
    Communicate with clients through phone, text, and email, providing exceptional customer service at all times.
    Use computer systems for administrative tasks and member communication.
    Learn about bone health, osteoporosis, and fracture prevention to better assist members.

Requirements:

    A bachelor''s degree in exercise science, kinesiology, sports science, or a related field is preferred, but not required.
    Relevant certifications such as Certified Personal Trainer (CPT) or Certified Strength and Conditioning Specialist (CSCS) are highly desirable, especially with a focus on senior fitness.
    Experience in coaching, personal training, or wellness is a plus.
    A strong interest in helping others, particularly an aging population, improve their lives.
    Excellent communication and interpersonal skills, with the ability to connect and motivate individuals of all fitness levels.
    Empathetic and compassionate approach, with a focus on creating a supportive environment.
    Strong organizational skills and attention to detail.
    Ability to work independently and collaborate within a team.

Benefits:

    Free access to Osteogenic Loading equipment for yourself and a significant other.
    Free access to our modalities: Red light therapy, hydromassage, PEMI therapy, compression therapy, vibration therapy, and X3 (variable resistance training program).

If you''re interested in making a difference in the lives of others and being part of a dynamic team, we’d love to hear from you. Please email your cover letter and resume to anchoragemidtown@osteostrong.me.

OsteoStrong® is an equal opportunity employer.'),
	(39, 'Administrative Coordinator', 'Bachelor''s degree in Business Administration, Finance, Accounting, or a related field preferred.
    Previous experience in administrative roles, with exposure to accounts payable/receivable, payroll, and financial management.
    Experience with donor databases (Little Green Light preferred).', 'Cleveland, OH', CURRENT_DATE, 'Position Type: Full-Time (40 hours per week)
Hourly Rate: $25
Schedule: Monday – Friday, 9:00 am – 5:00 pm
Reports to: Executive Director
Supervises: None

Description:
The Cleveland Kids’ Book Bank is seeking an Administrative Coordinator to play a key role in supporting the organization''s administrative operations. This position involves a range of responsibilities, including fiscal management, office coordination, donor database management, and assisting with HR and employee benefits. The ideal candidate will be highly organized, detail-oriented, and able to work efficiently in a fast-paced environment.

Key Responsibilities:

Fiscal Coordination:

    Process invoices, expense reports, and vendor payments accurately and on time.
    Monitor accounts receivable, follow up on outstanding payments, and maintain transaction records.
    Update QuickBooks software to track financial transactions, generate reports, and ensure accounting standards are met.
    Make bank deposits and manage petty cash, ensuring accurate reconciliations.
    Reconcile credit card statements and resolve discrepancies.
    Perform monthly bank and account reconciliations to ensure accuracy.

Donor Database Management:

    Maintain and update donor information in the organization’s database.
    Conduct regular audits and cleanups of the database to ensure data accuracy.
    Generate reports and donor acknowledgments as needed.

Human Resources and Benefits:

    Assist with HR duties, such as onboarding, maintaining employee records, and coordinating benefits enrollment.
    Help plan, execute, and track business and HR projects.
    Process payroll accurately and in compliance with applicable laws and regulations.
    Address employee payroll inquiries and maintain payroll records.

Office Management:

    Order office supplies and equipment, negotiating pricing and terms with vendors.
    Monitor inventory and place orders as needed.
    Coordinate meetings, conferences, and events, ensuring timely scheduling and material distribution.
    Prepare and edit documents, reports, and presentations.
    Provide administrative assistance to Directors and Managers, including calendar management, light travel arrangements, and expense reporting.
    Facilitate communication between departments to encourage collaboration and information sharing.

Qualifications:

	Proficiency in QuickBooks and Google Suite.
    Strong organizational and time management skills, with excellent attention to detail.
    Excellent communication and interpersonal abilities.
    Ability to multitask and prioritize effectively in a fast-paced environment.
    Knowledge of HR processes and benefits administration is a plus.

Benefits:

    Competitive salary
    Healthcare benefits
    Paid time off
    Professional development opportunities

Application Instructions:
To apply, please submit a resume and cover letter outlining your qualifications and interest in the position to hr@kidsbookbank.org.

Diversity & Inclusion:
We are committed to diversity, equity, and inclusion and encourage individuals from all backgrounds to apply. The Cleveland Kids’ Book Bank is an equal opportunity employer.'),
	(40, 'Content Writer', 'Proven experience in collaboration with clients and within an office environment.', 'Greater Philadelphia', CURRENT_DATE, 'Classification: Exempt
Band Description: Specialist
Supervisor: Director of Communications

Position Summary:
The Content Writer will develop and disseminate impactful written content for the United Methodists of EPA and GNJ, supporting the mission to recruit and equip transformational spiritual leaders. This position plays a key role in creating content to make disciples and grow vital congregations that transform the world. This is a collaborative role within the EPA&GNJ Communications Team.

Essential Functions:

    Craft and manage engaging content across various channels, aligning with the objectives of EPA&GNJ.
    Maintain the editorial calendar for EPA&GNJ.
    Oversee the production of the quarterly "NEWSpirit" newspaper, coordinating content, design, publication, distribution, and budget management while ensuring high production standards and fiscal responsibility.
    Manage, curate, and track the weekly "Digest" e-newsletter.
    Write editorial features highlighting local church ministries and conference initiatives.
    Revise written content from others to ensure consistency in style, fonts, images, and tone.
    Compile and produce publications like the AC Pre-Conference Workbooks and the AC Journal.
    Balance written and visual content to reflect diversity, intercultural competency, and theological differences within the conferences.

Organizational Responsibilities:

    Assist with related communications duties such as social media, photography, and representing the communications team on project teams.
    Serve as a participant or project manager for assigned projects.
    Assist in EPA & GNJ meetings and events.

Core Competencies:

    Committed to continuous growth in intercultural competence.
    Build and maintain relationships rooted in honesty, integrity, and confidentiality.
    Work collaboratively with others to produce innovative solutions.
    Demonstrate initiative and networking skills.
    Meet deadlines and efficiently convert ideas into stories that connect EPA&GNJ’s mission to action.

Qualifications:

    Portfolio of published articles (electronic and print).
    Excellent writing and editing skills in English.
    Hands-on experience with MailChimp, WordPress, SEO tools, Microsoft Suite, and social media platforms.
    Familiarity with web publications.
    Photography skills preferred.

Education:

    Bachelor’s degree in journalism, communications, or public relations.

Travel:
The position requires some evening and weekend responsibilities, as well as travel beyond the office. This is a hybrid role based in the EPA office in Norristown, PA and the GNJ office in Neptune, NJ.

Mission Alignment:
EPA & GNJ employees contribute to fulfilling the mission: to recruit and develop transformational leaders who make disciples and grow vital congregations to transform the world. The organization values:

    Innovation and risk-taking
    Excellence in ministry and service
    Compassionate and just service
    Diversity
    Collaboration

Application Instructions:
Inquiries and resumes should be sent to jkim@gnjumc.org until the position is filled.'),
	(41, 'Commercial Property Manager', 'Minimum of 5 years of experience in real estate accounting.', 'Birmingham, AL', CURRENT_DATE, 'Shannon Waltchack is seeking a Commercial Property Manager to manage a portion of its commercial real estate portfolio. This role will report to the VP of Finance & Administration (VP) and oversee the day-to-day responsibilities related to the accounting operations of our real estate portfolio. The ideal candidate will provide general oversight for various accounting functions, including Accounts Receivable, Accounts Payable, reconciliations, property financials, and other property accounting tasks. The Commercial Property Manager will also supervise staff as determined by the VP.

Essential Responsibilities:

    Develop, document, and implement internal controls for property management processes.
    Lead, manage, and hold accountable direct reports.
    Prepare, review, adjust, and post journal entries.
    Manage treasury operations, lender and bank reconciliations.
    Oversee charges and receipts for properties.
    Manage check runs, ACH payments, and approve wire transfers.
    Oversee financial statement reporting, accruals, and adjustments for properties.
    Compile quarterly asset management reports and process investor distributions.
    Supervise 1099 preparation and distribution.
    Oversee OPEX reconciliations.
    Oversee property contract administration and vendor compliance.
    Provide various forms of support to the VP, President, Partners, and Investors.

Preferred Qualifications:

    Bachelor’s degree in accounting or related discipline (preferred).
    Certified Public Accounting (CPA) designation (preferred).
    Ability to comprehend, analyze, and interpret real estate terms, principles, and documents.
    High degree of initiative, self-direction, and attention to detail.
    Excellent written and oral communication skills.
    Strong organizational and analytical skills.
    Proactive, responsive, and resourceful with the ability to multi-task and work well under pressure.
    Demonstrated proficiency with Microsoft Office 365 and Yardi Property Management Software.

Additional Skills:

    Strong interpersonal communication skills.
    Excellent organizational and time-management skills.
    Proficiency in Microsoft Word and Excel.'),
	(42, 'Physician Assistant', '1-2 years of practical experience in primary care settings', 'Atlanta, GA', CURRENT_DATE, 'We are seeking a qualified Physician Assistant or Nurse Practitioner with at least 1-2 years of practical experience in primary care settings to join our dynamic team. This position offers flexible employment options, with both part-time and full-time opportunities available.

Key Details:

    Hours: Monday through Friday, 8:30 AM to 5:30 PM, with optional additional hours every other Saturday from 9:00 AM to 2:00 PM.
    No On-Call Duty required.
    Compensation: Commensurate with experience.

Benefits:

    Paid vacation time
    Participation in a 401k retirement plan
    Comprehensive health insurance coverage

If you are a dedicated Primary Care Provider looking to make an impact in the Chamblee/Atlanta area, we invite you to apply and join our team!'),
	(43, 'NPE 2025 Exhibition Event Worker', NULL, 'Orlando, FL', CURRENT_DATE, 'Event Dates: May 6, 2025 (Mon) - May 10, 2025 (Fri)
Location: Orange County Convention Center (OCCC), 9800 International Drive, Orlando, FL 32819
Show Times: 9:00 AM – 5:00 PM (Closing early at 3:00 PM on the last day)

Job Description:
We are seeking 2-3 enthusiastic exhibition workers for NPE 2025. Responsibilities will include handing out flyers, encouraging visitors to fill out inquiry forms (with daily goals), and collecting business cards.

Requirements:

    Proficiency in English (Mandarin is a plus)
    Strong communication skills and attention to detail
    Available to work from 8:30 AM – 5:00 PM

Compensation:

    $100 USD per day
    Extra bonuses for good performance

Additional Information:

    An online interview will take place on Friday, April 19, 2025
    Pre-event training will occur the day before the exhibition at OCCC

If you''re interested, please send your resume to service@prm-taiwan.com with the subject line "Your Name - NPE 2025."

Contact:
Evelyn
Phone: +886 988 351 334

Note: The hours on the last day may be shorter, and fewer workers will be needed as the event progresses. Times are subject to change by the event organizers.'),
	(44, 'Software Engineer', 'Expertise in PHP development and a strong understanding of object-oriented programming principles. Experience with e-commerce platforms or related projects is preferred.', 'Denver, CO', CURRENT_DATE, 'GOYT is looking for a skilled and motivated PHP Software Developer to join our dynamic team. As a key contributor, you will help iterate and enhance our web-based product, driving the growth and success of our company.

Responsibilities:

    Develop and maintain high-quality PHP code for our web-based application
    Collaborate with the team to design and implement new features and improvements
    Troubleshoot and resolve issues to ensure optimal performance and reliability
    Contribute to the technical roadmap and decision-making processes to support company growth
    Stay up-to-date with industry trends and best practices to continually improve our product

Requirements:
    Proficiency in front-end technologies (HTML, CSS, JavaScript)
    Familiarity with MySQL or other relational databases
    Ability to work independently and as part of a remote team
    Excellent communication and collaboration skills
    Passion for learning and staying updated with emerging technologies

Benefits:

    Join a fast-growing startup and help shape its future
    Equity-based compensation package
    Flexible remote work environment
    Collaborative, supportive work culture
    Potential for professional growth and career advancement

If you’re an innovative PHP developer with a passion for growth, we’d love to hear from you! Please submit your resume and portfolio to business@goyt.com showcasing your relevant experience.'),
	(45, 'Swim Instructor', 'Previous experience in teaching swim lessons.', 'Harlingen, TX', CURRENT_DATE, 'Harlingen Country Club (HCC) is seeking professional and experienced private swim instructors to teach lessons at our club pool. We provide the clients, and you set your own schedule! This is a great opportunity for those who are passionate about swimming and teaching.

Responsibilities:

    Conduct private (1-on-1) and small group swim lessons for members
    Flexibility to work during morning hours
    Tailor lessons to the skill level and needs of each individual or group

Requirements:

    CPR certification
    Strong communication and interpersonal skills

Compensation:

    Earn up to $30/hr

How to Apply:
Interested candidates can email their resume to Estella@harlingencc.com.'),
	(46, 'Administrative Assistant', '3-5 years of proven office management, administrative, or assistant experience.', 'Woburn, MA', CURRENT_DATE, 'We are seeking an organized and efficient Administrative Assistant to support our growing nonprofit. In this hybrid role, you''ll be responsible for coordinating program administration and ensuring organizational effectiveness. The successful candidate will be a self-starter, capable of multitasking and managing tasks independently.

Duties and Responsibilities:

    Serve as the point person for mailing, shipping, ordering supplies, and errands
    Organize and schedule meetings and appointments
    Handle HR functions such as onboarding new employees into the payroll system
    Coordinate with IT providers on program equipment
    Manage vendor relationships, ensuring timely ordering, invoicing, and payment
    Negotiate contracts and pricing with office vendors and service providers
    Provide general support to callers and email contacts
    Maintain office filing systems and oversee clerical functions
    Develop standards and implement activities to improve operational procedures
    Monitor and maintain office supply inventory
    Ensure data security, integrity, and confidentiality
    Prepare operational reports and schedules to ensure efficiency
    Participate in program recruitment, orientation, and training
    Assist with company activities planning and execution
    Other duties as assigned

Qualifications:

    Minimum of an Associate''s degree in secretarial/office administration or equivalent experience
    Strong time management skills with the ability to multitask and prioritize
    Attention to detail and excellent problem-solving skills
    Excellent written and verbal communication skills
    Proficient in Microsoft Office
    Knowledge of office systems, HR management practices, and accounting procedures
    Strong organizational, planning, and interpersonal skills

Hours: 22.5 hours/week
Salary: $23.00/hr

Benefits:

    Prorated sick and vacation days
    11 paid holidays
    $0.50 per mile for work-related travel
    70% coverage of monthly health insurance premium

Other Requirements:

    Must be COVID vaccinated

How to Apply:
Please submit your resume and cover letter to [email/contact details].'),
	(47, 'Service / Construction Technician', 'Experience in HVAC or construction-related projects (preferred)', 'West Bridgewater, MA', CURRENT_DATE, 'We are looking for Service/Construction Technicians and Apprentices to join our team. This role involves:

    Performing inspections and maintenance of HVAC and refrigeration systems
    Planning and executing construction projects
    Ensuring compliance with construction safety protocols
    Assessing and surveying construction sites
    Maintaining accurate project documentation

Qualifications

- Knowledge of civil engineering and building surveying principles
- Understanding of construction safety protocols
- Strong problem-solving and analytical skills
- Attention to detail and ability to maintain documentation
- Excellent communication and teamwork abilities
- Physical fitness to work in various conditions
- OSHA certification or relevant licenses (preferred)
Benefits

- 401(k) plan
- Health, Dental, and Vision insurance
- Short- and Long-term disability coverage
- Company van and gas card (for qualified technicians)
- Paid vacation, holidays, and 40 hours of sick time
- End-of-year bonuses
How to Apply

Interested candidates can apply by [including instructions for application—email, online form, or phone contact].

Join Pierce Refrigeration and build a rewarding career with a company that values expertise, safety, and customer satisfaction!'),
	(48, 'Legal Secretary', 'Minimum of 2 years of Arizona or Colorado civil litigation experience.', 'Phoenix, AZ', CURRENT_DATE, 'A legal secretary/assistant is needed for the national litigation group of a Fortune 500 company. This position offers a competitive salary and superior benefits. Our firm represents one of the country’s leading title insurance companies, major institutional lenders, and property owners in real estate litigation matters.

The ideal candidate is a team player with experience managing a busy litigation desk and providing administrative support to experienced trial attorneys.
Requirements
    Knowledge of state and federal procedural rules
    Strong organizational skills and attention to detail
    Proficiency in MS Office Suite, including Adobe
    Experience with TurboCourt and e-filing (preferred)

How to Apply

Interested candidates should submit a resume, salary requirements, and references via email to Heidi.cooling@fnf.com.'),
	(49, 'Salesperson', '1-2 years of experience in a relevant role', 'United States', CURRENT_DATE, 'Requirements
    Ability and willingness to travel
    Strong communication and organizational skills
    Self-motivated and able to work independently

What We Offer

    Work-from-home flexibility
    Great bonus structure
    Opportunity to earn $100K+ immediately'),
	(49, 'Delegate Acquisition', '1-2 years of experience in a relevant role', 'United States', CURRENT_DATE, 'Requirements
    Ability and willingness to travel
    Strong communication and organizational skills
    Self-motivated and able to work independently

What We Offer

    Work-from-home flexibility
    Great bonus structure
    Opportunity to earn $100K+ immediately'),
	(49, 'Sales Support', '1-2 years of experience in a relevant role', 'United States', CURRENT_DATE, 'Requirements
    Ability and willingness to travel
    Strong communication and organizational skills
    Self-motivated and able to work independently

What We Offer

    Work-from-home flexibility
    Great bonus structure
    Opportunity to earn $100K+ immediately'),
	(50, 'Registered Nurse', NULL, 'Grayling, MI', CURRENT_DATE, 'Available Shifts & Sign-On Bonuses:

    1st Shift: $5,000 Sign-On Bonus
    3rd Shift: $10,000 Sign-On Bonus

About Atrium Centers

At Atrium Centers, we strive to be a light in the lives of our residents, their families, and our team members. Our mission is to provide compassionate, quality care in the communities we serve.
Benefits:

    100% Employee-Owned (ESOP) & 401(k) Matching
    Medical, Dental, Vision, & Life Insurance
    Paid Time Off & Holiday Pay
    Tuition Reimbursement – Advance Your Career with Our Support!
    Atrium Centers Discount Program – Save on travel, electronics, health & wellness, automotive, and more

Responsibilities:

    Assess, evaluate, and provide direct care based on residents'' care plans
    Administer medications and treatments per residents'' needs
    Supervise and evaluate nursing assistants

Qualifications:

    Current RN License
    Ability to administer medication and IV certification
    Strong understanding of State Rules & Regulations
    A positive, can-do attitude and reliable attendance

If you''re looking to make a meaningful impact while working in a supportive environment, we invite you to apply today!'),
	(51, 'Marketing & Office Coordinator', 'Minimum of 2 years of marketing/office coordinator experience', 'Denver, CO', CURRENT_DATE, 'Revesco Properties is a boutique commercial real estate firm specializing in investment, development, and management. Our operations include:

    Revesco Properties – Developing urban-infill projects that enhance Denver neighborhoods
    Revesco Properties Trust – Raising Canadian equity for open-air shopping centers and mixed-use properties
    The River Mile – A 62-acre redevelopment of Elitch Gardens in downtown Denver

Position Summary

We are seeking an experienced and versatile Marketing and Office Coordinator to support our marketing efforts and office operations. The ideal candidate is creative, highly organized, and thrives under tight deadlines. This role requires expertise in marketing execution, branding, content strategy, and office administration.
Marketing Responsibilities

    Marketing Strategies – Develop and execute marketing plans aligned with company objectives
    Brand Management – Ensure consistency across all marketing channels
    Campaign Execution – Plan and implement digital, print, social media, and event campaigns
    Content Strategy – Develop content for websites, social media, and email marketing
    Sales Collateral – Create brochures, product sheets, and presentations
    Event Management – Coordinate company events and partnerships with non-profits
    Analytics & Reporting – Track performance metrics and adjust strategies as needed
    Marketing Calendar – Maintain deadlines and provide updates to leadership
    CRM Software – Manage and utilize HubSpot for marketing initiatives

Office Responsibilities

    Event Planning – Organize office events, meetings, and logistics
    Office Management – Maintain office supplies, equipment, and vendor coordination
    Process Improvement – Identify and implement efficiency improvements
    Ad Hoc Support – Provide general administrative support as needed

Qualifications

    Bachelor’s degree in marketing, business, or related field
    Proficient in Adobe Creative Suite (InDesign, Illustrator, Acrobat)
    Strong Microsoft Office skills
    Excellent organizational skills, ability to multitask, and meet deadlines
    Creative thinker with experience in campaign development
    Strong business writing, editing, and proofreading skills
    Experience using CRM software, preferably HubSpot
    Notary certification or willingness to obtain one

Work Environment & Culture

    Office located in LoHi neighborhood with Little Owl Coffee in the building
    Team activities, including a summer boat day, ski trip, volunteer events, and weekly breakfast club

Compensation

 $55,000 – $75,000/year

If you are passionate about marketing, highly organized, and eager to grow with a dynamic team, we encourage you to apply!'),
	(52, 'Software Support Specialist', '1-2 years Experience in a Help Desk or customer support role', 'McLean, VA', CURRENT_DATE, 'Are you passionate about problem-solving and driven to provide exceptional support? Do you thrive in challenging environments that push you to grow?

My client, a leader in Spectrum Engineering and Management, is looking for a dynamic Software Support Specialist to join their team. If you''re goal-oriented, eager for new experiences, and ready to make an impact, we want to hear from you!
Responsibilities

    Assist users in designing and optimizing wireless networks
    Support web application users by identifying issues and testing updates/fixes
    Conduct online support sessions to troubleshoot and resolve technical concerns
    Contribute to RFI (Request for Information) and RFP (Request for Proposal) efforts
    Assist in sales initiatives and business development efforts

Required Skills & Qualifications

    Strong computer skills and technical aptitude
    Excellent verbal and written communication skills
    Bachelor’s degree in science or engineering (preferred)
    Ability to work autonomously and manage multiple tasks
    Knowledge of PHP, JavaScript, and web development (desirable)
    Spanish/Portuguese language skills (a plus)

If you have 1-2 years of experience in a support role or are a recent graduate eager to jumpstart your career, get in touch!'),
	(53, 'Coordinator for Multicultural Student Organizations', 'Experience with budget management and financial processes', 'Pullman, WA', CURRENT_DATE, 'The ASWSU Coordinator serves as the primary advisor to the ASWSU Senate, committees, and affiliated functions. This role requires a strong understanding of the ASWSU Constitution, By-laws, and University procedures to effectively guide and support student leadership.
Key Responsibilities

    Advise and support the ASWSU Senate, committees, and affiliated organizations
    Provide guidance on governance, policies, and procedures related to ASWSU operations
    Challenge and mentor student leaders, fostering their growth and development
    Assist students in budget appropriation, reconciliation, and financial management
    Support the planning and execution of ASWSU programs and services
    Collaborate with external advisors and university staff to enhance student engagement

Qualifications & Skills

    Strong knowledge of student government structures, policies, and procedures
    Ability to mentor, challenge, and support student leaders
    Excellent organizational, communication, and advising skills
    Ability to work collaboratively with students, staff, and external stakeholders

This is an excellent opportunity for someone passionate about student leadership development and university governance.'),
	(54, 'Barber', 'Experience preferred, but willing to train the right person.', 'Grafton, WI', CURRENT_DATE, 'A part-time barber position is now available, with exciting growth opportunities, including potential ownership, increased hours over time, or staying part-time based on preference.
Key Details:
    Perform all types of haircuts and some shaving (training provided)
    Schedule and manage clients
    References required

This is a great opportunity for someone looking to start or expand their barbering career with flexibility and long-term potential.');

    """)


def downgrade() -> None:
    pass
