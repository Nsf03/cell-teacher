"""Views for Cell Teacher application.

Provides views for displaying cell diagram, test page, and organelle information.
"""
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView


def home(request: HttpRequest):
    """Render home page with interactive cell diagram.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered home page template
    """
    return render(request, 'main/home.html')


def test(request: HttpRequest):
    """Render test page for organelle identification.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered test page template
    """
    return render(request, 'main/test.html')


def organelle_detail(request: HttpRequest, organelle_type: str):
    """Display detailed information about a specific organelle.
    
    Args:
        request: HTTP request object
        organelle_type: Type of organelle (nucleus, mitochondria, lysosome, membrane)
        
    Returns:
        Rendered organelle detail page with information
    """
    organelles_info = {
        'nucleus': {
            'name': 'Ядро (Nucleus)',
            'image': 'img/nuclear-info.jpg',
            'description': (
                'Ядро — это самая важная органелла клетки, содержащая '
                'генетическую информацию (ДНК). Оно отвечает за контроль '
                'всех жизненных процессов в клетке и передачу наследственной '
                'информации потомкам. Ядро ограничено ядерной мембраной и '
                'содержит хромосомы, которые хранят инструкции для синтеза белков.'
            )
        },
        'mitochondria': {
            'name': 'Митохондрия (Mitochondria)',
            'image': 'img/mito-info.jpg',
            'description': (
                'Митохондрии часто называют энергетическими станциями клетки. '
                'Они генерируют энергию (АТФ) в процессе клеточного дыхания, '
                'которая используется для всех энергозависимых процессов в клетке. '
                'Митохондрии имеют собственную ДНК и могут самостоятельно '
                'воспроизводиться. Их содержание выше в клетках с высокой '
                'энергетической активностью.'
            )
        },
        'lysosome': {
            'name': 'Лизосома (Lysosome)',
            'image': 'img/lyso-info.jpg',
            'description': (
                'Лизосомы содержат пищеварительные ферменты и отвечают за '
                'разложение и переваривание бактерий, отмершых органелл и других '
                'отходов, защищая клетку от вредных веществ. В среднем лизосома '
                'содержит около 50 различных ферментов, которые работают в '
                'кислой среде.'
            )
        },
        'membrane': {
            'name': 'Клеточная мембрана (Cell Membrane)',
            'image': 'img/memb-info.png',
            'description': (
                'Клеточная мембрана представляет собой тонкий слой, окружающий '
                'клетку и разделяющий внутреннюю среду от внешней. Она состоит '
                'из липидов и белков и выполняет защитную и регуляторную функцию. '
                'Мембрана селективно пропускает вещества, контролируя обмен между '
                'клеткой и её окружением.'
            )
        }
    }

    organelle = organelles_info.get(organelle_type, {
        'name': organelle_type.title(),
        'image': '',
        'description': 'Информация об этой органелле недоступна.'
    })

    context = {
        'organelle_type': organelle_type,
        'organelle': organelle
    }
    return render(request, 'main/organelle_detail.html', context)