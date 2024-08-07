from allscreen.lcm.lcm import LCMView
from allscreen.hcf.hcf import HCFView
from allscreen.bmi.bmi import BMIView
from allscreen.XOGame.xo_game import XOView
from allscreen.AgeFinder.age_finder import AgeFinderView
from allscreen.Area.area import AreaView
from allscreen.CompareFraction.compare_fraction import CompareFractionView
from allscreen.Flames.flames import FlamesView
from allscreen.FractionCalculator.fraction_calculator import FractionCalculatorView
from allscreen.MatrixTypeFinder.matrix_type_finder import MatrixTypeFinderView
from allscreen.MatrixCalculator.matrix_calculator import MatrixCalculatorView
from allscreen.PercentageCalculator.percentage_calculator import PercentageCalculatorView
from allscreen.PercentageToPart.percentage_to_part import PercentageToPartView
from allscreen.Perimeter.perimeter import PerimeterView
from allscreen.Ratio.ratio import RatioView
from allscreen.SimpleCompoundInterest.si_ci import SimpleCompoundInterestView
from allscreen.SudokuPuzzleSolver.sudoku_puzzle_solver import SudokuPuzzleSolverView
from allscreen.SurfaceArea.surface_area import SurfaceAreaView
from allscreen.UnitConverter.unit_converter import UnitConverterView
from allscreen.Volume.volume import VolumeView
#from allscreen.About.about import AboutView
from allscreen.NotePad.note_pad import NotePadView


screens={
    
    "lcm":{
        "view":LCMView,
        "kv":"allscreen/lcm/lcm.kv"
    },
    "hcf":{
        "view":HCFView,
        "kv":"allscreen/hcf/hcf.kv"
    },
    "bmi":{
        "view":BMIView,
        "kv":"allscreen/bmi/bmi.kv"
    },
    "xo":{
        "view":XOView,
        "kv":"allscreen/XOGame/xo_game.kv"
    },
    "fraction":{
        "view":FractionCalculatorView,
        "kv":"allscreen/FractionCalculator/fraction_calculator.kv"
    },
    "comp_fraction":{
        "view":CompareFractionView,
        "kv":"allscreen/CompareFraction/compare_fraction.kv"
    },
    "matrix":{
        "view":MatrixCalculatorView,
        "kv":"allscreen/MatrixCalculator/matrix_calculator.kv"
    },
    "type_matrix":{
        "view":MatrixTypeFinderView,
        "kv":"allscreen/MatrixTypeFinder/matrix_type_finder.kv"
    },
    
    "conversion":{
        "view":UnitConverterView,
        "kv":"allscreen/UnitConverter/unit_converter.kv"
    },
    "percentage":{
        "view":PercentageCalculatorView,
        "kv":"allscreen/PercentageCalculator/percentage_calculator.kv"
    },
    "tax":{
        "view":PercentageToPartView,
        "kv":"allscreen/PercentageToPart/percentage_to_part.kv"
    },
    "si":{
        "view":SimpleCompoundInterestView,
        "kv":"allscreen/SimpleCompoundInterest/si_ci.kv"
    },
    "ratio":{
        "view":RatioView,
        "kv":"allscreen/Ratio/ratio.kv"
    },
    "age":{
        "view":AgeFinderView,
        "kv":"allscreen/AgeFinder/age_finder.kv"
    },
    "sudoku":{
        "view":SudokuPuzzleSolverView,
        "kv":"allscreen/SudokuPuzzleSolver/sudoku_puzzle_solver.kv"
    },
    "flames":{
        "view":FlamesView,
        "kv":"allscreen/Flames/flames.kv"
    },
    "note_pad":{
        "view":NotePadView,
        "kv":"allscreen/NotePad/note_pad.kv"
    },
    "peri_2d":{
        "view":PerimeterView,
        "kv":"allscreen/Perimeter/perimeter.kv"
    },
    "area_2d":{
        "view":AreaView,
        "kv":"allscreen/Area/area.kv"
    },
    "area_3d":{
        "view":SurfaceAreaView,
        "kv":"allscreen/SurfaceArea/surface_area.kv"
    },
    "vol_3d":{
        "view":VolumeView,
        "kv":"allscreen/Volume/volume.kv"
    },

}

"""
"about":{
        "view":AboutView,
        "kv":"allscreen/About/about.kv"
    },
"""


    
    
    