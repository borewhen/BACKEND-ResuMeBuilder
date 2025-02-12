"""Added more jobs and companies

Revision ID: b6677f870b41
Revises: 30529347fd00
Create Date: 2025-02-12 07:17:23.667669

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6677f870b41'
down_revision: Union[str, None] = '79127f7cb87f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
INSERT INTO public.companies (name, industry, address, website_url, logo_url, description)
VALUES 
    ('Corcoran Sawyer Smith', 'Real Estate', 'Princeton, NJ', 'https://www.corcoran.com/corcoran-sawyer-smith/26', NULL, 'Corcoran is a thoroughly modern real estate company built on traditional values of service, integrity, market expertise, and neighborhood fluency.'),
    ('The National Exemplar', 'Restaurant', 'Mariemont, OH', 'https://www.nationalexemplar.com/home/', NULL, 'The National Exemplar is a restaurant located in Mariemont, Ohio, offering classic American cuisine in a cozy atmosphere.'),
('Abrams Fensterman, LLP', 'Law Firm', 'Brooklyn, NY', 'https://www.abramslaw.com/', NULL, 'Abrams Fensterman is a full-service law firm providing a range of legal services to clients across various industries.'),
    ('Downtown Raleigh Alliance', 'Non-Profit Organization', 'Raleigh, NC', 'https://downtownraleigh.org/', NULL, 'The Downtown Raleigh Alliance is dedicated to advancing the vitality of downtown Raleigh through various programs and initiatives.'),
	('Raw Cereal', 'Design', 'Los Angeles, CA 90017, US', 'https://www.rawcereal.com/', NULL, 'Raw Cereal is a creative production company that creates immersive experiences for the world''s best known artists and brands.'),
    ('Children''s Nebraska', 'Healthcare', 'Omaha, NE', 'https://www.childrensnebraska.org/', NULL, 'Children''s Nebraska provides comprehensive pediatric healthcare services to children across the state.'),
    ('Bay West Church', 'Religion', 'Melbourne, FL', 'https://baywestchurch.churchcenter.com/', NULL, 'Bay West Church is a community-focused church offering worship services and various community programs.'),
	 ('Glastender, Inc.', 'Manufacturing', 'Saginaw, MI', 'https://www.glastender.com/', NULL, 'Glastender designs and manufactures bar and restaurant equipment, providing innovative solutions for the foodservice industry.'),
	 ('PGAV Destinations', 'Architecture & Design', 'St. Louis, MO', 'https://pgavdestinations.com/', NULL, 'PGAV Destinations specializes in planning and designing unique destinations, including museums, theme parks, and zoos.'),
	 ('Staffing Theory', 'Recruiting', 'Raleigh, NC', 'https://www.staffingtheory.com/', NULL, 'Staffing Theory is a niche recruiting partner for the biopharma industry.'),
	 ('OsteoStrong', 'Health & Wellness', 'Australia', 'https://www.osteostrong.me/', NULL, 'OsteoStrong offers a unique system for strengthening bones, joints, and muscles through specialized equipment and sessions.'),
	 ('CLEVELAND KIDS BOOK BANK', 'Non-Profit Organization', 'Cleveland, OH', 'https://www.kidsbookbank.org/', NULL, 'The Cleveland Kids'' Book Bank provides free books to children in need to foster literacy and a love of reading.'),
	 ('United Methodists of Greater New Jersey', 'Religion', 'Neptune City, NJ', 'https://www.gnjumc.org/', NULL, 'The United Methodists of Greater New Jersey oversee and support Methodist congregations and ministries within the region.'),
	 ('Shannon Waltchack', 'Real Estate', 'Birmingham, AL', 'https://shanwalt.com/', NULL, 'Shannon Waltchack is a commercial real estate firm offering brokerage, property management, and investment services.'),
	 ('Premier Family Clinic', 'Healthcare', 'Chamblee, GA', NULL, NULL, 'Premier Family Clinic provides primary care services to patients in the Chamblee/Atlanta area.'),
	 ('PRM-TAIWAN', 'Manufacturing', 'Taiwan', 'https://www.prm-taiwan.com/', NULL, 'PRM-TAIWAN is a B2B platform for the plastic and rubber machinery industry, connecting global buyers with Taiwanese manufacturers.'),
	 ('GOYT', 'Technology', 'Dallas, Texas', 'https://www.linkedin.com/company/goyt', NULL, 'GOYT is a saas platform that helps e-commerce websites increase conversion rates by using curated videos from social platforms. '),
	 ('Harlingen Country Club', 'Hospitality', 'Harlingen, TX', 'https://www.harlingencc.com/', NULL, 'Harlingen Country Club offers golf, dining, and recreational facilities to its members and guests.'),
	 ('REquipment, Inc.', 'Non-Profit Organization', 'Canton, MA', 'https://dmereuse.org/', NULL, 'REquipment provides refurbished durable medical equipment to individuals in need, promoting environmental responsibility and accessibility.'),
	 ('Pierce Refrigeration', 'Heating, Ventilation, and Air Conditioning (HVAC) Services', 'Brockton, MA', 'https://piercerefrig.com/', NULL, 'Pierce Refrigeration provides HVAC services, including installation and maintenance, to residential and commercial clients.'),
	 ('Fidelity National Title Insurance Company', 'Title Insurance and Legal Services', 'Jacksonville, FL', 'https://www.fntic.com/', NULL, 'Fidelity National Title offers title insurance and related services, ensuring the efficient transfer of real estate.'),
	 ('ABME', 'Advertising', 'New York', 'https://www.linkedin.com/company/abmmediagroup', NULL, 'ABME is a leading B2B marketing and media company specializing in providing C-level engagement with the world’s largest brands and executives. With a combined 50+ years of industry experience, we have created a community of some of the top technology executives in the world. Through these communities, we are able to deliver custom, results-oriented marketing solutions. Whether you’re looking to support your demand generation, relationship building, brand awareness, sales revenue, or market research, our custom events give you the tools and information you need to impact your target audience and ultimately your organizations bottom line.'),
	 ('Atrium Centers', 'Healthcare', 'Columbus, OH', 'https://atriumlivingcenters.com/', NULL, 'Atrium Centers operates skilled nursing facilities, providing long-term care and rehabilitation services.'),
	 ('Revesco Properties', 'Real Estate', 'Denver, CO', 'https://www.revescoproperties.com/', NULL, 'Revesco Properties is a real estate investment firm focusing on the acquisition and management of retail and mixed-use properties.'),
	 ('Recruitment Design', 'Recruiting', NULL, 'https://recruitmentdesign.com/', NULL, 'Achieve success and scale your company with Recruitment Design’s tailored solutions. We empower growing companies with agile and smart talent acquisition strategies, offering innovative sourcing methods, personalized service, and a commitment to excellence.'),
	 ('Washington State University', 'Higher Education', 'Pullman, WA', 'https://wsu.edu/', NULL, 'Washington State University is a public research university offering a wide range of undergraduate and graduate programs.'),
	 ('Headquarters Barbershop', 'Personal Grooming Services', 'Fascinatio Boulevard 494, Capelle aan den IJssel', 'https://www.hq-barbershop.nl/', NULL, 'We provide exceptional grooming services for the discerning modern gentleman. Our barbershop is designed with a sophisticated and elegant atmosphere that exudes a sense of luxury and relaxation.'),
	 ('navXcom', 'Telecommunications', 'Houston', 'https://www.navxcom.com/', NULL, 'navXcom specializes in advanced communication solutions, focusing on navigation and communication technologies.'),
	 ('Diment & Associates', 'Consulting', '3445 North Causeway Blvd., Suite 724, Metairie, LA 70', 'https://dimentfirm.com/', NULL, 'Diment & Associates provides strategic consulting services across various sectors, assisting businesses in achieving their goals.'),
	 ('LT Apparel Group', 'Apparel & Fashion', 'New York, NY, USA', 'https://www.ltapparel.com/', NULL, 'LT Apparel Group designs, sources, and markets children''s apparel, offering a range of brands and products.'),
	 ('ViaBot', 'Robotics', 'San Francisco, CA, USA', 'https://viabot.com/', NULL, 'ViaBot develops robotic solutions for outdoor maintenance, aiming to automate tasks like sweeping and snow removal.'),
	 ('City of Germantown, TN', 'Government', 'Germantown, TN, USA', 'https://www.germantown-tn.gov/', NULL, 'The City of Germantown provides municipal services to its residents, including public safety, parks, and community development.'),
	 ('Lead Lab', 'Marketing', 'Studio 1, Rollsbridge House, Exeter, Devon, EX2 9QU', 'http://www.theleadlab.com/', NULL, 'Lead Lab specializes in lead generation and marketing strategies to help businesses increase their customer base.'),
	 ('Saxon AI', 'Artificial Intelligence', 'N-Heights Building, 2A Plot No, 12, Software Units Layout, Madhapur, Hyderabad, Telangana 500081, India', 'https://saxon.ai/', NULL, 'Saxon AI focuses on developing AI-driven solutions to optimize business processes and decision-making.'),
	 ('Elica Electric Co', 'Electrical Manufacturing', '18712 SE 65th Place, Issaquah, WA 98006', 'https://www.elica.com/', NULL, 'Elica Electric Co manufactures electrical components and appliances, catering to various industrial needs.'),
	 ('USLI', 'Insurance', 'Wayne, PA, USA', 'https://www.usli.com/', NULL, 'USLI offers a range of insurance products, focusing on small businesses and nonprofit organizations.'),
	 ('NLB Services', 'Recruiting', 'Alpharetta, GA, USA', 'https://www.nlbservices.com/', NULL, 'NLB Services provides workforce solutions, including staffing, consulting, and outsourcing services across various industries.'),
	 ('KeyBank', 'Banking', 'Cleveland, OH, USA', 'https://www.key.com/personal/index.html', NULL, 'KeyBank offers a broad range of financial services, including personal banking, commercial banking, and investment management.'),
	 ('Polyram Plastic Industries Ltd', 'Manufacturing', 'Ram On, Israel', 'https://polyram-group.com/', NULL, 'Polyram specializes in the production of high-performance thermoplastic compounds for various applications.'),
	 ('Starup Insurance', 'Insurance', '3101 Park Boulevard Palo Alto, CA 94306', 'https://www.starupinsurance.com/', NULL, 'Starup Insurance provides a range of insurance products and services to individuals and businesses.'),
	 ('StyleAI', 'Fashion Technology', '300 Beale St # A, San Francisco, CA 94105, United States', 'https://styleai.io/', NULL, 'StyleAI integrates artificial intelligence into fashion, offering solutions like personalized styling and trend analysis.');
    """)
    op.execute("""
INSERT INTO public.jobs (company_id, title, experience_level, location, date_of_listing, description)
VALUES 
    ((SELECT company_id FROM public.companies WHERE name = 'Corcoran Sawyer Smith'), 'Marketing Coordinator', 'Marketing (1 year preferred), Graphic Design (2 years preferred)', 'Princeton, NJ', CURRENT_DATE, 'A leading real estate firm in New Jersey is seeking an administrative Marketing Coordinator with some experience in graphic design. You will be working closely with our fun, kind, ambitious members of the sales team and our dynamic executive team on a daily basis. This is an opportunity to be part of a fast-growing, highly respected real estate brokerage with a reputation for exceptional marketing and extraordinary culture of cooperation and inclusion. You must be a well-organized, creative, proactive, positive, and most importantly, kind-hearted person. Please, be responsible, respectful, and cool-under-pressure. Please, be proficient in Adobe Creative Cloud (Indesign, Illustrator, Photoshop) and Microsoft Office Suite. Above all, have fantastic taste and be a good-hearted, fun-loving person who loves working with people and is eager to learn. Our office is a fast-paced environment. You will work directly with a Marketing team and communicate daily with other core staff and our large team of agents. This description is a brief overview, but your skills and interests will be considered in what you work on and as the role evolves over time. Agent Assistance - Receive & Organize Marketing Requests from Agents. Track Tasks & Communicate with Marketing team & Agents on Status - Prepare print materials and signs for open houses- Submit Orders to Printers & Communicate & Track Deadlines Graphic Design & Branding - Managing brand strategy and messaging through website, social media, videos, online advertising, print placement and events. Receive, organize, and prioritize marketing requests from agents. Fulfill agent design requests including postcards, signs, email marketing and property brochures using pre-existing templates and creating custom designs. Maintain brand assets and generic files. Events & Community - Plan and execute events and promotions, Manage Contacts & Vendors for Event Planning & Sponsorships. Our company is committed to creating a diverse environment and is proud to be an equal opportunity employer. All qualified applicants will receive consideration for employment without regard to race, color, religion, gender, gender identity or expression, sexual orientation, national origin, genetics, disability, age, or veteran status. Pay: $18-20/hour. Expected hours: 35 to 45 per week. Benefits: Paid time off. Schedule: 8 hour shift, Monday to Friday.'),
	((SELECT company_id FROM public.companies WHERE name = 'The National Exemplar'), 'Assistant Restaurant Manager', 'Prefer 1 to 3 years FOH management experience.', 'Cincinnati, OH', CURRENT_DATE, 'The National Exemplar is accepting applications for an Assistant Restaurant Manager. We offer highly competitive wages, healthcare, paid time off, complimentary dining privileges and bonus opportunities. We are a serious, professional, long-standing neighborhood restaurant with over 41 years of service. If you are looking for a long-term fit with a best in class organization then you should apply now. Please send a resumes to pardom@nationalexemplar.com. Candidate should be a self-starter, proactive, attentive to details and like developing others. Must have a strong sense of teamwork and strong witten and verbal communication skills. Have a keen interest in service, food and learning. Passion for excellence and doing things right.'),
	((SELECT company_id FROM public.companies WHERE name = 'Abrams Fensterman, LLP'), 'Senior Elder Law / Trusts and Estates Associate Attorney', '10-15 years of experience, Experience with various advance directives, trusts, and wills.', 'New Hyde Park, NY', CURRENT_DATE, 'Senior Associate Attorney - Elder Law / Trusts and Estates. Our legal team is committed to providing each client with quality counsel, innovative solutions, and personalized service. Founded in 2000, the firm offers the legal expertise of its 115+ attorneys, who have accumulated experience and problem-solving skills over decades of practice. We are a prominent Lake Success Law Firm seeking an associate attorney for its growing Elder Law and Estate Planning practice. The successful candidate will be a self-motivated, detail-oriented team member with strong communication skills and a desire to grow their practice. Experience with Estate Planning, Administration, and Litigation and is preferred. Responsibilities will include: Counseling clients with regard to estate planning and asset protection; Formulating and overseeing execution of Medicaid and estate plans;Drafting wills, revocable and irrevocable trusts, powers of attorney, health care proxies, and living wills; Estate Administration; Trust Administration; Court Appearances for Estate and Proceedings; Supervising paralegals. 
Qualifications: Juris Doctor degree (J.D.) from an accredited law school. Licensed to practice law in New York. Strong analytical and problem-solving skills. Ability to build rapport with clients. Excellent written and verbal communication skills. Competitive salary commensurate with experience. Salary: $140,000- $175,000. Benefits: 401k, Medical, Dental, Life Insurance, PTO, and more. This position is based out of Lake Success, NY. This position requires a baseline understanding of online marketing including Search Engine Marketing, Search Engine Optimization, and campaign analytics. The ideal candidate must be an analytical and detailed dynamic, self-starter who is proactive, and able to multitask effectively. This individual must be a strategic thinker with excellent verbal and written communication, as well strong presentation skills and the ability to work independently in an organized manner.'),
	((SELECT company_id FROM public.companies WHERE name = 'Downtown Raleigh Alliance'), 'Economic Development and Planning Intern', NULL, 'Raleigh, NC', CURRENT_DATE, 'Job Summary:
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
	((SELECT company_id FROM public.companies WHERE name = 'Raw Cereal'), 'Producer', NULL, 'United States', CURRENT_DATE, 'Company Description

Raw Cereal is a creative design agency specializing in live, interactive, corporate, and installation-based entertainment. Our mission is to push boundaries and create unique and immersive experiences for our clients. We pride ourselves on our end-to-end creative services and cutting-edge use of technology for larger-than-life productions.

Role Description

We''re looking for Directors, Producers, Creatives, AI Programmers, 3D Artists, Senior Motion Graphics Artists, Editors, etc. If you think you have something to add, please reach out.

Email: Jobs@rawcereal.com'),
	((SELECT company_id FROM public.companies WHERE name = 'Children''s Nebraska'), 'Respiratory Therapist', 'Minimum one year of experience in respiratory therapy (Preferred), Experience working with pediatric patients (Preferred)', 'Omaha, NE', CURRENT_DATE, 'Company Description

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
	((SELECT company_id FROM public.companies WHERE name = 'Bay West Church'), 'Worship Leader', 'At least two years of experience in general office responsibilities and procedures, and two years of experience in graphic design and media.', 'Palm Bay, FL', CURRENT_DATE, 'We''re excited about the future of our church, and we''re looking for a passionate and energetic leader to help us make disciples for Jesus in Palm Bay, Florida, and beyond.

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
	((SELECT company_id FROM public.companies WHERE name = 'Glastender, Inc.'), 'Inside Customer Service Associate', 'Experience in a business sales environment or college coursework in business and marketing is a plus. Previous customer service experience required.', 'Saginaw, MI', CURRENT_DATE, 'Glastender Inc. is a family-owned manufacturer of top-quality commercial bar and restaurant equipment, providing innovative solutions to the industry for over 50 years. We''re dedicated to delivering exceptional customer experiences and are currently seeking an Inside Customer Service Associate to join our team.

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
	((SELECT company_id FROM public.companies WHERE name = 'Glastender, Inc.'), 'Production Supervisor', 'A college degree or 5-7 years of related work experience.', 'Saginaw, MI', CURRENT_DATE, 'Glastender Inc. is seeking a Production Supervisor with strong leadership and organizational skills to manage our production team and processes. This role requires the ability to meet specific production targets and efficiently manage resources.

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
	((SELECT company_id FROM public.companies WHERE name = 'PGAV Destinations'), 'Project Architect', 'Bachelor’s or Master’s degree in Architecture from an accredited institution. 5-10 years of experience working in an architectural firm.', 'St Louis, MO', CURRENT_DATE, 'PGAV Destinations is looking for a self-motivated and highly creative individual with a solid understanding of architectural technical aspects. The ideal candidate should be quick to learn, collaborative, and possess a strong work ethic, with the ability to manage multiple projects simultaneously. You will play an integral role in coordinating complex, design-intensive projects, guiding less experienced teammates along the way. The role will involve all stages of design, from concept to construction documentation and administration.

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
	((SELECT company_id FROM public.companies WHERE name = 'Staffing Theory'), 'Senior Product Marketing Manager', 'Minimum of 7 years of experience in pharmaceutical product marketing, with a proven track record of success. Experience in immunology, and preferably gastroenterology.', 'United States', CURRENT_DATE, 'A leading pharmaceutical company, dedicated to developing and commercializing innovative, high-quality medicines that improve patient lives, is seeking a Senior Product Marketing Manager. This role will be responsible for creating and executing marketing strategies for one or more pharmaceutical products. The ideal candidate will work closely with cross-functional teams—such as sales, medical affairs, market research, and commercial operations—to develop and implement integrated marketing plans that drive product awareness, adoption, and revenue growth.

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
	((SELECT company_id FROM public.companies WHERE name = 'OsteoStrong'), 'Osteogenic Loading Coach', 'Customer service: 1 year (preferred). Health, fitness, or medical: 1 year (preferred)', 'Anchorage, AK', CURRENT_DATE, 'OsteoStrong® is a unique wellness center focused on strengthening the skeletal system, which is the foundation of the body. Unlike a gym, diet, or medical treatment, OsteoStrong® offers a proven strategy to improve bone density, posture, balance, athletic performance, and reduce joint and back pain. We work with individuals of all ages, helping them strengthen their bones using a method called Osteogenic Loading, which delivers measurable results quickly.

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
	((SELECT company_id FROM public.companies WHERE name = 'CLEVELAND KIDS BOOK BANK'), 'Administrative Coordinator', 'Bachelor''s degree in Business Administration, Finance, Accounting, or a related field preferred.
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
	((SELECT company_id FROM public.companies WHERE name = 'United Methodists of Greater New Jersey'), 'Content Writer', 'Proven experience in collaboration with clients and within an office environment.', 'Greater Philadelphia', CURRENT_DATE, 'Classification: Exempt
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
	((SELECT company_id FROM public.companies WHERE name = 'Shannon Waltchack'), 'Commercial Property Manager', 'Minimum of 5 years of experience in real estate accounting.', 'Birmingham, AL', CURRENT_DATE, 'Shannon Waltchack is seeking a Commercial Property Manager to manage a portion of its commercial real estate portfolio. This role will report to the VP of Finance & Administration (VP) and oversee the day-to-day responsibilities related to the accounting operations of our real estate portfolio. The ideal candidate will provide general oversight for various accounting functions, including Accounts Receivable, Accounts Payable, reconciliations, property financials, and other property accounting tasks. The Commercial Property Manager will also supervise staff as determined by the VP.

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
	((SELECT company_id FROM public.companies WHERE name = 'Premier Family Clinic'), 'Physician Assistant', '1-2 years of practical experience in primary care settings', 'Atlanta, GA', CURRENT_DATE, 'We are seeking a qualified Physician Assistant or Nurse Practitioner with at least 1-2 years of practical experience in primary care settings to join our dynamic team. This position offers flexible employment options, with both part-time and full-time opportunities available.

Key Details:

    Hours: Monday through Friday, 8:30 AM to 5:30 PM, with optional additional hours every other Saturday from 9:00 AM to 2:00 PM.
    No On-Call Duty required.
    Compensation: Commensurate with experience.

Benefits:

    Paid vacation time
    Participation in a 401k retirement plan
    Comprehensive health insurance coverage

If you are a dedicated Primary Care Provider looking to make an impact in the Chamblee/Atlanta area, we invite you to apply and join our team!'),
	((SELECT company_id FROM public.companies WHERE name = 'PRM-TAIWAN'), 'NPE 2025 Exhibition Event Worker', NULL, 'Orlando, FL', CURRENT_DATE, 'Event Dates: May 6, 2025 (Mon) - May 10, 2025 (Fri)
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
	((SELECT company_id FROM public.companies WHERE name = 'GOYT'), 'Software Engineer', 'Expertise in PHP development and a strong understanding of object-oriented programming principles. Experience with e-commerce platforms or related projects is preferred.', 'Denver, CO', CURRENT_DATE, 'GOYT is looking for a skilled and motivated PHP Software Developer to join our dynamic team. As a key contributor, you will help iterate and enhance our web-based product, driving the growth and success of our company.

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
	((SELECT company_id FROM public.companies WHERE name = 'Harlingen Country Club'), 'Swim Instructor', 'Previous experience in teaching swim lessons.', 'Harlingen, TX', CURRENT_DATE, 'Harlingen Country Club (HCC) is seeking professional and experienced private swim instructors to teach lessons at our club pool. We provide the clients, and you set your own schedule! This is a great opportunity for those who are passionate about swimming and teaching.

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
	((SELECT company_id FROM public.companies WHERE name = 'REquipment, Inc.'), 'Administrative Assistant', '3-5 years of proven office management, administrative, or assistant experience.', 'Woburn, MA', CURRENT_DATE, 'We are seeking an organized and efficient Administrative Assistant to support our growing nonprofit. In this hybrid role, you''ll be responsible for coordinating program administration and ensuring organizational effectiveness. The successful candidate will be a self-starter, capable of multitasking and managing tasks independently.

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
	((SELECT company_id FROM public.companies WHERE name = 'Pierce Refrigeration'), 'Service / Construction Technician', 'Experience in HVAC or construction-related projects (preferred)', 'West Bridgewater, MA', CURRENT_DATE, 'We are looking for Service/Construction Technicians and Apprentices to join our team. This role involves:

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
	((SELECT company_id FROM public.companies WHERE name = 'Fidelity National Title Insurance Company'), 'Legal Secretary', 'Minimum of 2 years of Arizona or Colorado civil litigation experience.', 'Phoenix, AZ', CURRENT_DATE, 'A legal secretary/assistant is needed for the national litigation group of a Fortune 500 company. This position offers a competitive salary and superior benefits. Our firm represents one of the country’s leading title insurance companies, major institutional lenders, and property owners in real estate litigation matters.

The ideal candidate is a team player with experience managing a busy litigation desk and providing administrative support to experienced trial attorneys.
Requirements
    Knowledge of state and federal procedural rules
    Strong organizational skills and attention to detail
    Proficiency in MS Office Suite, including Adobe
    Experience with TurboCourt and e-filing (preferred)

How to Apply

Interested candidates should submit a resume, salary requirements, and references via email to Heidi.cooling@fnf.com.'),
	((SELECT company_id FROM public.companies WHERE name = 'ABME'), 'Salesperson', '1-2 years of experience in a relevant role', 'United States', CURRENT_DATE, 'Requirements
    Ability and willingness to travel
    Strong communication and organizational skills
    Self-motivated and able to work independently

What We Offer

    Work-from-home flexibility
    Great bonus structure
    Opportunity to earn $100K+ immediately'),
	((SELECT company_id FROM public.companies WHERE name = 'ABME'), 'Delegate Acquisition', '1-2 years of experience in a relevant role', 'United States', CURRENT_DATE, 'Requirements
    Ability and willingness to travel
    Strong communication and organizational skills
    Self-motivated and able to work independently

What We Offer

    Work-from-home flexibility
    Great bonus structure
    Opportunity to earn $100K+ immediately'),
	((SELECT company_id FROM public.companies WHERE name = 'ABME'), 'Sales Support', '1-2 years of experience in a relevant role', 'United States', CURRENT_DATE, 'Requirements
    Ability and willingness to travel
    Strong communication and organizational skills
    Self-motivated and able to work independently

What We Offer

    Work-from-home flexibility
    Great bonus structure
    Opportunity to earn $100K+ immediately'),
	((SELECT company_id FROM public.companies WHERE name = 'Atrium Centers'), 'Registered Nurse', NULL, 'Grayling, MI', CURRENT_DATE, 'Available Shifts & Sign-On Bonuses:

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
	((SELECT company_id FROM public.companies WHERE name = 'Revesco Properties'), 'Marketing & Office Coordinator', 'Minimum of 2 years of marketing/office coordinator experience', 'Denver, CO', CURRENT_DATE, 'Revesco Properties is a boutique commercial real estate firm specializing in investment, development, and management. Our operations include:

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
	((SELECT company_id FROM public.companies WHERE name = 'Recruitment Design'), 'Software Support Specialist', '1-2 years Experience in a Help Desk or customer support role', 'McLean, VA', CURRENT_DATE, 'Are you passionate about problem-solving and driven to provide exceptional support? Do you thrive in challenging environments that push you to grow?

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
	((SELECT company_id FROM public.companies WHERE name = 'Washington State University'), 'Coordinator for Multicultural Student Organizations', 'Experience with budget management and financial processes', 'Pullman, WA', CURRENT_DATE, 'The ASWSU Coordinator serves as the primary advisor to the ASWSU Senate, committees, and affiliated functions. This role requires a strong understanding of the ASWSU Constitution, By-laws, and University procedures to effectively guide and support student leadership.
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
	((SELECT company_id FROM public.companies WHERE name = 'Headquarters Barbershop'), 'Barber', 'Experience preferred, but willing to train the right person.', 'Grafton, WI', CURRENT_DATE, 'A part-time barber position is now available, with exciting growth opportunities, including potential ownership, increased hours over time, or staying part-time based on preference.
Key Details:
    Perform all types of haircuts and some shaving (training provided)
    Schedule and manage clients
    References required

This is a great opportunity for someone looking to start or expand their barbering career with flexibility and long-term potential.'),
	((SELECT company_id FROM public.companies WHERE name = 'navXcom'), 'Barber', 'Experience with mobile app development (Android/iOS preferred)', 'United States', CURRENT_DATE, 'Are you passionate about cutting-edge software development for deep space communication and navigation systems? Are you eager to jumpstart your career and be part of an innovative NASA project?

We are looking for a talented Computer Scientist to join our team on a voluntary (unpaid) basis and help develop a mobile application to support this mission.
Responsibilities:

    Collaborate with engineers, software developers, and product managers
    Develop and implement feature-rich, secure software
    Contribute to the design and functionality of the mobile application
    Work on real-world space technology challenges

Requirements:

    Background in computer science, software engineering, or related field
    Strong understanding of security and performance optimization
    Passion for space exploration and cutting-edge technology

This is an exciting opportunity to gain hands-on experience and contribute to a groundbreaking project.'),
	((SELECT company_id FROM public.companies WHERE name = 'Diment & Associates'), 'Client Relations Specialist', NULL, 'Baton Rouge, LA', CURRENT_DATE, 'Are you a high-energy, customer-focused professional with a passion for sales and client engagement? Do you thrive in a fast-paced, dynamic environment where exceptional performance is rewarded?

We are a regional law firm looking for a driven candidate with uncommon initiative, strong interpersonal skills, and a commitment to excellence. This is a client-facing role, and we take that responsibility seriously.
Responsibilities:

    Answer and manage incoming phone calls professionally
    Schedule and set appointments on the appropriate calendar
    Communicate case updates to clients
    Greet clients upon arrival and ensure a welcoming experience
    Maintain detailed notes and statuses on interactions
    Communicate professionally with all parties who contact the firm

What We’re Looking For:

    Superior phone sales experience and a passion for closing deals
    Strong organizational skills, multitasking ability, and attention to detail
    Exceptional communication skills—both written and verbal
    A highly motivated and results-driven individual
    Ability to work efficiently in a fast-paced, no-nonsense environment

Fair Warning Disclaimer:

    This role includes a 90-day trial period. Performance will be evaluated, and continued employment is not guaranteed if expectations are not met.
    If retained after 90 days, you will be eligible for performance incentives and benefits.

Benefits (After 90-Day Trial):

    Paid Time Off (PTO)
    Health, Vision, and Dental Insurance
    401(k) with match after first anniversary
    Incentive pay based on performance

This is not an average job for an average candidate. If you are exceptional, ambitious, and ready to excel, apply today!'),
	((SELECT company_id FROM public.companies WHERE name = 'LT Apparel Group'), 'Intern- Business Analytics', NULL, 'Greensboro--Winston-Salem--High Point Area', CURRENT_DATE, 'Location: LT Apparel, Greensboro, NC

Are you a data-driven problem solver with a passion for analytics? Do you want to gain real-world experience in the fast-paced apparel industry? We are looking for a bright, motivated MBA intern to join our team and help streamline our costing process while building predictive models for improved efficiency.
Responsibilities:

    Collaborate with the global sourcing team to review current costing models and identify areas for process improvement.
    Develop and implement predictive product costing models to enhance forecasting accuracy.
    Conduct data analysis to uncover trends in material and production costs across different sourcing regions.

Qualifications:

    Currently enrolled in an MBA program with a focus on data analytics.
    Strong academic record with proficiency in data analysis, modeling, and visualization techniques.
    Experience with data visualization tools (e.g., Tableau, Power BI).
    Advanced Microsoft Excel skills (including complex formulas and functions).
    Ability to translate complex data into actionable insights.
    Excellent communication and teamwork skills.
    A creative and innovative approach to problem-solving is a plus.

What We Offer:

    Hands-on experience with two major brands (adidas & Carhartt).
    Collaboration with industry experts in both sourcing and data analytics.
    Competitive internship stipend.
    A fun, fast-paced, and collaborative work environment.

How to Apply:

Submit your resume to catherine.lim@ltapparel.com.'),
	((SELECT company_id FROM public.companies WHERE name = 'ViaBot'), 'Robot Monitor & Maintenance Technician', NULL, 'Sunnyvale, CA', CURRENT_DATE, 'Join ViaBot, the first autonomous property management solution for commercial properties! We are seeking a Robot Monitor & Maintenance Technician to work 2nd/3rd shift (7 PM - 3 AM, Thursday - Monday). This role involves monitoring multiple robots, reporting issues, and performing basic diagnostics and maintenance.
Responsibilities:

    Monitor our robot fleet remotely, ensuring they operate efficiently.
    Report technical issues to the engineering team.
    Maintain property cleanliness if the robot is unable to perform its duties.
    Perform basic diagnostic checks and fixes (training provided).

Qualifications:

    Tech-savvy, with the ability to use multiple applications.
    Ability to multi-task and work independently.
    Comfortable working on a computer for most of the shift.
    Able to lift 20+ lbs when required.
    Must have U.S. work authorization.

Preferred (Not Required):

    Experience with hand/power tools.
    Background in electronic/mechanical system troubleshooting.

Benefits:

    $20.00/hour starting pay.
    Health, Dental, Vision Insurance.
    Flexible schedule & paid time off.
    Health savings & flexible spending accounts.
    Life insurance.

Work Schedule:

    5-day workweek (full-time only).
    Must work Friday & one weekend day.
    Priority given to those who can work Friday-Sunday regularly.

Application Questions:

    Are you able to work 7 PM - 3 AM?
    What is your earliest start date?
    Are you comfortable monitoring robots on a computer for most of the shift?
    Which days off do you prefer?

Apply today and be part of the future of autonomous property management!'),
	((SELECT company_id FROM public.companies WHERE name = 'City of Germantown, TN'), 'Director of Public Works', 'Seven years of experience in public works activities, with at least three years in a managerial role.', 'Germantown, TN', CURRENT_DATE, 'The City of Germantown is seeking a Public Works Director to plan, organize, and direct the operations of the Public Works Department, including the construction, maintenance, and repair of city streets, storm drains, and sewer systems, solid waste management, and the operation of water treatment plants. This role will involve a durational partnership with the Executive Director of Public Works until their retirement in 2025.
Essential Job Functions:

    Plan, direct, and coordinate public works functions including street maintenance, sewer systems, storm drains, solid waste management, and municipal water systems.
    Collaborate with city engineers in planning, designing, and inspecting public works projects.
    Develop and implement department policies, goals, and objectives in alignment with city mission.
    Prepare and manage the department’s budget and capital improvement programs, and oversee grant-funded initiatives.
    Negotiate and manage public works contracts, including solid waste collection and recycling.
    Respond to citizen inquiries, complaints, and ensure compliance with laws, regulations, and city codes.
    Represent the city in public works on local, state, and national boards and committees.

Knowledge, Skills, and Abilities:

    Knowledge of engineering principles related to public works and infrastructure systems.
    Expertise in municipal laws, sanitary sewer systems, water distribution, and solid waste operations.
    Strong communication skills for negotiating, justifying, and reporting significant issues.
    Ability to plan, manage, and evaluate the work of others, and work cooperatively with city officials, employees, and the public.

Qualifications:

    Bachelor’s degree in engineering or a related field. Advanced degrees in engineering, management, or public administration are desirable.
    A combination of education, training, and experience may be considered.

Working Conditions:

    Primarily office-based with considerable outdoor work on-site to inspect projects.
    Occasional exposure to extreme weather and physical tasks like walking, standing, bending, and climbing.
    Travel is required for meetings and conferences.

Application Process:

Submit your application today to become part of a team committed to enhancing the quality of life for the City of Germantown residents through excellence in public works management.'),
	((SELECT company_id FROM public.companies WHERE name = 'Lead Lab'), 'Digital Marketing Intern', NULL, 'Redmond, WA', CURRENT_DATE, 'Duration: 12 weeks (Starting May-June)
Pay: $25/hr, 25 hours/week
Position Overview:

We are seeking a creative, self-motivated Marketing Intern to join our small yet dynamic digital marketing team. The internship will focus primarily on organic marketing efforts, where you’ll work directly with our team on day-to-day tasks and deliverables.
Responsibilities:

    Social Media Management: Assist in managing and organizing the content calendar.
    Content Creation: Design and write engaging social media posts across various platforms.
    Email Marketing: Create and send out monthly newsletters.
    Blog Posts: Craft compelling and informative blog content.
    Video Production: Produce short-form videos for platforms like TikTok, Facebook, and Instagram.
    Web Design: Contribute to ongoing web design projects.

Who We Are:

We are a digital marketing and lead generation company based in Redmond, WA. Our focus is on online lead generation through paid advertising, but we also help clients with social media marketing, web design, and email marketing campaigns.

On a typical day, we’re focused on:

    Developing creative copy for ad campaigns.
    Exploring new marketing trends.
    Designing landing pages and diving into reports.

We take our work seriously, but never ourselves, offering our team opportunities for personal and professional growth.
Who You Are:

    A self-starter who enjoys taking initiative and ownership of tasks.
    A strong writer and effective communicator.
    Eager to learn and always willing to think creatively.
    Comfortable with switching gears and adapting quickly.
    Bring new ideas to the table and enjoy a good challenge.
    Have a good sense of humor and a strong grasp of GIF culture (essential for Slack communication).
    Bonus points if you have a Goodreads account (we''re kidding… kind of).

Logistics:

    Duration: 12 weeks (May-June start)
    Hours: 25 hours/week
    Pay: $25/hr
    Schedule: Hybrid in-person/remote (full remote option available)
    Location: Must be a full-time resident of WA or SC.

How to Apply:

    Send your resume and your top three strengths to support@theleadlab.us.
    No cover letter is required!

Join us this summer and get hands-on experience in digital marketing and lead generation while working with a fun and supportive team!'),
	((SELECT company_id FROM public.companies WHERE name = 'Saxon AI'), 'Data Architect', 'Strong hands-on experience with AWS services (EC2, S3, Lambda, Glue, Athena, Kinesis, etc.).', 'San Francisco, CA', CURRENT_DATE, 'Job Description:

We are looking for an experienced Data Architect to join our team for a contract role in San Francisco, CA. This position involves working with a variety of AWS services and implementing solutions that require expertise in ETL, data warehousing, and cloud computing.
Key Responsibilities:

    Work with AWS services like EC2, S3, Lambda, Glue, Athena, Kinesis Data Streams, Kinesis Firehose, and more.
    Design and implement ETL processes and Data Warehousing solutions.
    Leverage SQL, Redshift, Python, SPARK, and JSON to build and manage data pipelines and integrations.
    Ensure API-based integration and security for data systems.
    Work with cloud computing and big data concepts to architect scalable and efficient solutions.

Required Skills & Experience:

    Strong hands-on experience with AWS services (EC2, S3, Lambda, Glue, Athena, Kinesis, etc.).
    Extensive experience in ETL & Data Warehousing concepts.
    Proficiency in SQL, Redshift, Python, SPARK, and JSON.
    Knowledge of API-based integration and security protocols.
    Familiarity with Cloud computing and Big Data concepts.

How to Apply:

Please send your resume to sunil.k@saxonglobal.com.

We look forward to hearing from you!'),
	((SELECT company_id FROM public.companies WHERE name = 'Elica Electric Co'), 'Motion Graphic Designer and Film Editor', 'Experience in the electrical engineering industry is a plus.', 'New York, NY', CURRENT_DATE, 'Elica Electric Co. is an electrical engineering company founded in 2010, based in Isfahan, Iran. We specialize in providing Schneider Electric, ABB, and Finder products. Schneider Electric offers energy and automation digital solutions for efficiency and sustainability. Our goal is to provide original products and excellent technical support to our customers.
Role Description:

We are seeking a Motion Graphic Designer and Film Editor to join our team on a full-time, on-site basis. The successful candidate will be responsible for creating motion graphics, video production, graphic design, and editing visual elements for various projects.
Key Responsibilities:

    Design and edit motion graphics for various projects.
    Handle video production and post-production tasks.
    Create and design visual elements to support marketing and engineering projects.
    Collaborate with team members and take direction for project execution.
    Ensure all visuals align with the company’s brand guidelines and standards.

Qualifications:

    Strong skills in Motion Design and Motion Graphics.
    Proficiency in Video Production and Editing.
    Expertise in Graphic Design and creating visuals.
    Proficient in Adobe Creative Suite (After Effects, Premiere Pro, Illustrator, Photoshop).
    Attention to detail with the ability to meet deadlines.
    Strong communication skills and the ability to work collaboratively.

If you are passionate about creating engaging motion graphics and video content, we encourage you to apply and join our dynamic team!'),
	((SELECT company_id FROM public.companies WHERE name = 'USLI'), 'Senior Developer', '10+ years of software development experience.', 'Greater Philadelphia', CURRENT_DATE, 'At USLI, we prioritize diversity, equity, and inclusion, creating a welcoming environment for individuals of all backgrounds. We offer a comprehensive benefits package, access to wellness programs, and resources for professional development. Our mission is to strengthen our community and culture, and we are committed to fostering a sense of belonging for all employees.
Role Overview:

We are looking for an experienced Senior Software Developer to join our high-performance team. In this Team Lead role, you will be responsible for overseeing medium-sized team initiatives, mentoring developers, and guiding the creation and maintenance of applications for mobile, web, and in-house systems. You will leverage your technical expertise and leadership skills to ensure timely and quality delivery of software solutions, while fostering collaboration within your team.
Responsibilities:

    Lead day-to-day initiatives for medium-sized team projects.
    Use your proficiency in .NET and deep understanding of system architecture to design and implement new features.
    Maintain coding standards and ensure they are applied consistently within the team.
    Mentor and support other team members, resolving conflicts and promoting collaboration.
    Assist in recommending refactoring strategies and improvements to complex systems and workflows.
    Provide feedback to people leaders on developer performance.
    Continuously learn and stay updated with new technologies and software development trends.
    Act as a recognized expert in one or more technology disciplines (e.g., ASP.NET, C#, MVC).
    Ensure the successful implementation of design patterns (e.g., Singleton, Factory).
    Foster a culture of knowledge-sharing, particularly on complex technical topics.

Qualifications:
    College degree or equivalent technical certifications/industry experience.
    Proficient knowledge of the .NET framework, including ASP.NET, C#, MVC, and VB.NET.
    Strong experience with Agile/SCRUM methodologies and modern technologies like Angular.js, Knockout.js, and jQuery.
    Experience working with SQL Server, SQL/XML, and JavaScript/jSON.
    Ability to design, develop, and implement new features independently with minimal architectural guidance.
    Strong problem-solving and critical-thinking skills.
    Ability to work well in a team environment, providing guidance to both senior and junior developers.
    Excellent oral and written communication skills.

Working Hours:

    9:00 a.m. – 5:00 p.m., with occasional overtime as needed.

Additional Information:

    75% on-site work required.
    Competitive salary and benefits package.
    Opportunities for professional growth, mentoring, and continued education.

If you are a dynamic and experienced software developer ready to lead and mentor a team, we encourage you to apply and become part of the USLI family.'),
	((SELECT company_id FROM public.companies WHERE name = 'NLB Services'), 'Java architect / Lead Java developer', 'Proven experience in Java platform development.', 'Jersey City, NJ', CURRENT_DATE, 'Skills Required:

    Java
    Microservices
    REST APIs & Web Services
    UI Development - React JS, Redux, Micro Frontend
    Typescript, React.js

Job Description:

We are seeking a Java Architect / Lead Java Developer to join our team for a full-time position based in New Jersey. This role involves hands-on work with Java for backend development, as well as React JS for front-end components. The ideal candidate will have experience in designing and developing microservices architectures and implementing REST APIs and web services.

Additionally, the candidate should have prior experience in managing teams (either as a Lead or Engineering Manager), working in both onshore and offshore environments. A solid understanding of React.js, Redux, and Typescript is essential for UI development, while exposure to micro frontend will be a plus.
Key Responsibilities:

    Lead and architect Java-based applications and microservices.
    Implement REST APIs and web services.
    Collaborate with front-end teams using React.js and Redux for UI components.
    Design and manage complex systems with microservices architecture.
    Guide and mentor teams, managing both onshore and offshore resources.
    Ensure quality code development, adhering to best practices and design patterns.

Qualifications:

    Proven experience in Java platform development.
    Hands-on experience with React.js, Redux, Typescript, and Micro Frontend.
    Strong background in microservices and API development.
    Experience in leadership roles (e.g., Lead Developer or Engineering Manager) with offshore and onshore team management.
    Ability to architect and design complex systems and applications.

How to Apply:

Please send your updated resume to deepak.badhwar@nlbtech.com.'),
	((SELECT company_id FROM public.companies WHERE name = 'KeyBank'), 'Enterprise Data & Analytics Infrastructure Manager', 'Proven experience in managing data infrastructure and analytics teams.', 'Cleveland, OH', CURRENT_DATE, 'Job Description:

We are seeking an experienced Enterprise Data Infrastructure and Analytics Manager to lead a highly talented and motivated team responsible for supporting KeyBank’s data and analytics program. This role involves driving the stability, security, and modernization of the enterprise data infrastructure while building a strong talent pipeline. You will play a key role in the long-term strategy and development of our data platforms, ensuring they are scalable and reliable to support the bank''s business operations.
Key Responsibilities:

    Lead and manage a team of engineers focused on enhancing infrastructure support for KeyBank’s data and analytics program.
    Drive stability, security, and modernization of data and analytics platforms.
    Build and foster a talent pipeline for the team, ensuring that the necessary skills and capabilities are available for future challenges.
    Collaborate with stakeholders to align infrastructure strategies with business goals.
    Oversee the design, implementation, and continuous improvement of data infrastructure and analytics platforms.
    Ensure infrastructure is reliable, secure, and scalable to support the bank''s growing data needs.

Qualifications:

    Proven experience in managing data infrastructure and analytics teams.
    Strong knowledge of enterprise data platforms, security protocols, and cloud technologies.
    Experience driving modernization efforts and scaling infrastructure programs.
    Ability to mentor and develop a strong engineering team.
    Excellent communication and collaboration skills.

If you''re interested in more details, feel free to reach out!'),
	((SELECT company_id FROM public.companies WHERE name = 'Polyram Plastic Industries Ltd'), 'Brand Representative', NULL, 'United States', CURRENT_DATE, 'We are looking for a proactive, results-driven Sales Manager to represent our Engineering Thermoplastics Compounds (EP) and Polytron LFT in the USA. This individual will work independently to develop new markets, expand client relationships, and drive project generation within the engineering thermoplastics sector.
Roles & Responsibilities:

    Market Development: Identify and create new market opportunities for EP and Polytron LFT in relevant applications.
    Client Relationship Expansion: Strengthen existing customer relationships and actively seek out new clients to grow the customer base.
    Project Generation: Lead the creation of new project opportunities that align with the company''s strategic goals.
    Target-Oriented Approach: Demonstrate a focus on achieving and surpassing sales targets.
    Budget Management: Present and adhere to annual budgets to ensure optimal resource allocation and financial performance.

Skills and Knowledge Required:

    Educational Background: A degree in plastics engineering, materials science, or an MBA is a plus.
    Industry Acumen: Strong understanding of global industry standards, particularly in dealings with Tier 1 suppliers and OEMs.
    International Sales Experience: Proven track record in international sales, ideally with experience collaborating with companies like Polyram.
    Proactive Mindset: Self-driven with the ability to recognize and seize opportunities.
    Independence: Able to work independently and take initiative.
    Interpersonal Skills: Excellent relationship-building skills with clients and colleagues.
    Negotiation Expertise: Skilled in negotiation to secure favorable contracts and deals.
    Industry Knowledge: Experience with thermoplastics, ideally in automotive, firearms, sporting goods, or electronics & electricals.
    Travel Flexibility: Willingness to travel frequently as required by the role.

Professional Traits:

    Strong commitment to service excellence, reliability, and assertiveness in sales activities.

Preferred Background:
Candidates with experience in sectors like automotive, firearms, sporting goods, and electronics & electricals are encouraged to apply.
Why Join Us:

Be part of a dynamic team that drives innovation and growth in the engineering thermoplastics industry. Apply now to take your career to the next level!'),
	((SELECT company_id FROM public.companies WHERE name = 'Starup Insurance'), 'User Experience Designer', NULL, 'California, United States', CURRENT_DATE, 'Startup Insurance is a personalized health and wellbeing solution created by founders, for founders. We aim to protect venture-backed founders from burnout through concierge services and embedded insurance products. Our offering is available in multiple markets, including California, New York, Iowa, Dubai, Abu Dhabi, and Riyadh.
Role Description:

We are looking for a User Experience Designer to join our team on a contract remote basis. As a User Experience Designer, you will be responsible for creating intuitive and visually appealing user interfaces using design thinking principles. Your work will include conducting user research, developing visual designs, and prototyping user experiences. You will collaborate closely with cross-functional teams to ensure a seamless, user-centered design process.
Responsibilities:

    User Research & Design Thinking: Conduct user research to identify needs, pain points, and goals, applying design thinking principles to create solutions.
    Visual Design & UX: Develop visual designs that are aesthetically pleasing and meet user needs while ensuring a high-quality user experience.
    Prototyping: Create prototypes to test and refine design ideas.
    Collaboration: Work closely with product managers, developers, and other teams to ensure designs are practical and aligned with business goals.

Qualifications:

    User Research & Design Thinking: Experience in conducting user research and applying design thinking methodologies.
    Visual Design & UX: Strong skills in visual design and user experience (UX) to create intuitive interfaces.
    Prototyping: Proficiency in prototyping tools and techniques.
    Cross-functional Teamwork: Experience working in a cross-functional team, including product managers and developers.
    Problem-Solving: Strong problem-solving skills with an ability to tackle complex design challenges.
    Communication & Collaboration: Excellent communication skills to collaborate effectively across teams.
    UI/UX Design Tools: Familiarity with industry-standard UI/UX design tools (e.g., Figma, Sketch, Adobe XD, etc.).

Why Join Us:

Work in a fast-paced, innovative environment, designing products that help founders protect their mental and physical health, all while contributing to the growth of a company that truly cares about its users.'),
	((SELECT company_id FROM public.companies WHERE name = 'StyleAI'), 'Senior Software Engineer', '8+ years of experience in software development with a strong track record of launching innovative products from 0 to 1 and scaling them.', 'San Francisco Bay Area', CURRENT_DATE, 'Company Overview: StyleAI is an AI-powered, all-in-one unified marketing platform designed for businesses and ambitious marketing teams. With products like Seona, Crafta, and Adwin, StyleAI helps businesses automate their entire digital marketing strategy. Thousands of companies rely on StyleAI to manage SEO, Google Ads, and websites in real-time.

Key Highlights:

    Strategic Investors: Over $6M raised from investors including HOF Capital, Avenir, and General Catalyst, along with partnerships with Semrush and SimilarWeb.
    Exceptional Product Market Fit: From $0 to $3M ARR in just 12 months.
    Strong Talent Density: The team was founded by 2 Berkeley dropouts, with many members having turned down offers from major tech companies like Airbnb, Microsoft, and Palantir.

Mission: To democratize digital marketing for businesses of all sizes, empowering small businesses to create a strong online presence.
About the Role:

As an early member of the engineering team at StyleAI, you will play a pivotal role in building and scaling our core products, Crafta, Seona, and Adwin. This role offers the opportunity for early ownership and growth within a fast-paced startup environment. You will be responsible for both frontend and backend development, tackling technical challenges, and collaborating cross-functionally with the team.

The role is based in San Francisco, CA, and relocation assistance is available.
Responsibilities:

    Build intuitive, user-first web apps that scale with StyleAI’s growing user base.
    Collaborate with engineering teams to deliver the infrastructure for core and emerging products.
    Solve complex technical problems independently or as part of a team to deliver impactful solutions.
    Maintain and optimize core infrastructure.
    Ensure all production code is high-quality and meets team standards.

Qualifications:

    8+ years of experience in software development with a strong track record of launching innovative products from 0 to 1 and scaling them.
    Startup mindset: Scrappy, intelligent, and entrepreneurial, with a willingness to take on responsibility and grow with the company.
    Tech stack: Experience with Typescript/Javascript (frontend), Golang (backend), Kafka (job queuing system), PostgreSQL, and GCP. Experience with Golang and GCP is a bonus.
    Experience in building and scaling SaaS products with a strong attention to detail.
    Track record of shipping and scaling consumer tools or SMB-focused platforms is a plus.

Compensation:

    Expected salary: $200,000+
    Opportunity to participate in the company’s equity plan.
    Salary details may vary depending on career level, responsibilities, and experience.

Additional Information:

    Website: StyleAI
    Tenets: StyleAI Tenets
    Company Culture: Learn more about our culture

Join our mission to revolutionize digital marketing and drive growth for small businesses around the world!');
	""")


def downgrade() -> None:
    pass
