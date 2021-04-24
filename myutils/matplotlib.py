import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib_inline.backend_inline import set_matplotlib_formats

__all__ = [
    'matplotlib_latex',
    'matplotlib_svg',
    'matplotlib_dark_theme',
    'matplotlib_light_theme',
    'matplotlib_seaborn_style',
]

white = 'white'
black = '.1'
lightgray = 'lightgray'

dark_theme_rcparams = {
    "lines.color": white,
    "patch.edgecolor": white,
    "text.color": white,
    "axes.facecolor": black,
    "axes.edgecolor": lightgray,
    "axes.labelcolor": white,
    "axes.titlecolor": white,
    "xtick.color": white,
    "ytick.color": white,
    "grid.color": lightgray,
    "figure.facecolor": black,
    "figure.edgecolor": black,
    "savefig.facecolor": black,
    "savefig.edgecolor": black,
}

light_theme_rcparams = {
    key: plt.rcParamsDefault[key]
    for key in dark_theme_rcparams.keys()
}

latex_rcparams = {
    'text.usetex': True,
    'text.latex.preamble': '\\usepackage[utf8]{inputenc}\n\\usepackage[russian]{babel}',
}

serif_rcparams = {
    'font.family': [
        'serif'
    ],
    'font.serif': [
        'Computer Modern Roman',
        'Times',
        'Palatino',
        'New Century Schoolbook',
        'Bookman',
    ],
}


def matplotlib_latex(serif: bool = True):
    plt.rcParams.update(latex_rcparams)

    if serif:
        plt.rcParams.update(serif_rcparams)


def matplotlib_svg():
    set_matplotlib_formats('svg')


def matplotlib_seaborn_style(palette: str = 'deep'):
    plt.style.use('seaborn-whitegrid')
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=sns.color_palette(palette))
    plt.rcParams['grid.linestyle'] = 'dotted'


def matplotlib_dark_theme():
    plt.rcParams.update(dark_theme_rcparams)


def matplotlib_light_theme():
    plt.rcParams.update(light_theme_rcparams)
