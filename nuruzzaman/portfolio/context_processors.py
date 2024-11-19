# context_processors.py
from .models import LanguageSkill, HardSkill, PersonalInfo, KnowledgeItem

def global_context(request):
    language_skills = LanguageSkill.objects.all()
    hard_skills = HardSkill.objects.all()
    personal_info = PersonalInfo.objects.first()
    knowledge_items = KnowledgeItem.objects.all()  # Fetch knowledge items
    return {
        'language_skills': language_skills,
        'hard_skills': hard_skills,
        'personal_info': personal_info,
        'knowledge_items': knowledge_items,  # Add knowledge items to context
    }
