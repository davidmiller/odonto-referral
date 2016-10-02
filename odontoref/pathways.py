"""
Pathways for our application
"""
from pathway import pathways

class ReferralPathway(pathways.Pathway):
    template_url = "/templates/odonto_referral_pathway.html"
    display_name='Referral'
    slug='referral'
    steps = (
        pathways.Step(
            title="Your Details",
            template_url='/templates/your_details.html'
        ),
        pathways.Step(
            title="Relationship",
            template_url='/templates/relationship.html'
        ),
        pathways.Step(
            title="Referral Details",
            template_url='/templates/referral_details.html'
        ),
        pathways.Step(
            title="Urgency",
            template_url='/templates/urgency.html'
        ),
        pathways.Step(
            title="Patient Details",
            template_url='/templates/patient_details.html'
        ),
        pathways.Step(
            title="Send",
            template_url='/templates/summary.html'
        )
    )
