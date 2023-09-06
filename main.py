import random
import sympy
from sympy import Symbol
import matplotlib as mpl
mpl.rcParams['backend'] = "agg"
import matplotlib.pyplot as plt

class Problems:
    def random_exclude(self, exclude, range):
        exclude = set(exclude)
        randInt = random.randint(range[0],range[1])
        return self.random_exclude(exclude, range) if randInt in exclude else randInt 

    def midpoint(self, p1, p2):
        return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

    def generate_surd(self, intercept, exclude=[], base=None, range=(2, 6)):
        if base == None:
            base = random.choice([2, 3, 5])
        
        mult = self.random_exclude(exclude, range)

        surd = sympy.sqrt(base*(mult**2))+intercept

        return {
            "base": base,
            "mult": mult,
            "intercept": intercept,
            "sympy": surd,
            "latex": sympy.latex(surd),
            "evaluated": surd.evalf()
        }
    def missingHypotenuse(self):

        # Given 2 sides, find the hypotenuse

        pid = random.randint(1000, 9999)
    
        fig, ax = plt.subplots()

        ax.set_aspect('equal')

        line1data = self.generate_surd(0)
        line2data = self.generate_surd(0, exclude=[line1data["mult"]])

        answer = sympy.sqrt(sympy.Pow(line1data["sympy"], 2) + sympy.Pow(line2data["sympy"], 2))

        midpoint = self.midpoint((2, 2+line2data["evaluated"]), (2+line1data["evaluated"], 2))

        ax.plot([2, 2+line1data["evaluated"]], [2, 2], color="black")
        ax.plot([2, 2], [2, 2+line2data["evaluated"]], color="black")
        ax.plot([2, 2+line1data["evaluated"]], [2+line2data["evaluated"], 2], color="black")

        ax.axis('off')

        plt.text(2+line1data["evaluated"]/2, 1.9, "$"+line1data["latex"]+"$", horizontalalignment="center", verticalalignment="top", fontsize="x-large")
        plt.text(1.9, 2+line2data["evaluated"]/2, "$"+line2data["latex"]+"$", horizontalalignment="right", verticalalignment="top", fontsize="x-large")
        plt.text(midpoint[0]+0.1, midpoint[1], "$x$", horizontalalignment="left", verticalalignment="bottom", fontsize="xx-large")

        plt.xticks([])
        plt.yticks([])

        plt.savefig(f"media/problems/P{pid}.png")

        return {
            "id": pid,
            "type": "findhypotenuse",
            "problem": "\\text{The following triangle with side lengths }"+line1data['latex']+"\\text{ and }"+line2data['latex']+"\\text{, find the length of the hypotenuse.}",
            "answer": sympy.latex(answer.simplify())
        }
    
    def easySimplify(self):

        # Solve for the most simplified surd

        pid = random.randint(1000, 9999)

        a = self.generate_surd(0, range=(2, 9))
        b = self.generate_surd(0, exclude=[a["mult"]], base=a["base"], range=(2, 9))
        c = self.generate_surd(0, exclude=[a["mult"], b["mult"]], base=a["base"], range=(2, 9))

        packed = [a, b, c]
        newlist = sorted(packed, key=lambda d: d['mult']) 
        biggest = newlist[2]
        newlist.remove(biggest)

        with sympy.evaluate(False):

            newlist[0]["sympy"] = sympy.sqrt(newlist[0]["base"]*(newlist[0]["mult"]**2))
            newlist[1]["sympy"] = sympy.sqrt(newlist[1]["base"]*(newlist[1]["mult"]**2))
            biggest["sympy"] = sympy.sqrt(biggest["base"]*(biggest["mult"]**2))

            if bool(random.getrandbits(1)):
                top = newlist[1]["sympy"] - newlist[0]["sympy"]
            else:
                top = newlist[0]["sympy"] + newlist[1]["sympy"]

            answer = top/biggest["sympy"]

        return {
            "id": pid,
            "type": "easysimplify",
            "problem": "\\text{Fully simplify }"+sympy.latex(answer),
            "answer": sympy.latex(answer.simplify())
        }
    def rationaliseDenominator(self):

        # Rationalise the denominator for 

        pid = random.randint(1000, 9999)

        a = self.generate_surd(random.randint(1, 5), range=(1, 2))
        numer = random.randint(2, 8)

        answer = numer/a["sympy"]

        return {
            "id": pid,
            "type": "rationalisedenominator",
            "problem": "\\text{Rationalise the denominator for }"+sympy.latex(answer),
            "answer": sympy.latex(answer.simplify())
        }
    
    def expressAbAb(self):

        # Express (a+b)/(a-b)

        pid = random.randint(1000, 9999)

        baseSurd = self.generate_surd(random.randint(1, 5), range=(1, 3))
        
        with sympy.evaluate(False):
            radical = sympy.sqrt(baseSurd["base"]*baseSurd["mult"]**2)
            intercept = baseSurd["intercept"]
            final = (intercept-radical)/(intercept+radical)

            a = Symbol("a")
            b = Symbol("b")

            form = a+b*sympy.sqrt(baseSurd["base"])

        return {
            "id": pid,
            "type": "rationalisedenominator",
            "problem": "\\text{Express }"+sympy.latex(final)+"\\text{ in the form }"+sympy.latex(form),
            "answer": sympy.latex(final.simplify())
        }

problems = Problems()

problems.expressAbAb()