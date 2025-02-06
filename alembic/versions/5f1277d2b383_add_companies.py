"""Add companies

Revision ID: 5f1277d2b383
Revises: 79127f7cb87f
Create Date: 2025-02-06 14:18:57.019494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f1277d2b383'
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
		('Headquarters Barbershop', 'Personal Grooming Services', 'Fascinatio Boulevard 494, Capelle aan den IJssel', 'https://www.hq-barbershop.nl/', NULL, 'We provide exceptional grooming services for the discerning modern gentleman. Our barbershop is designed with a sophisticated and elegant atmosphere that exudes a sense of luxury and relaxation.');
	""")
    
	

def downgrade() -> None:
	pass
    
