from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import cmath

app = FastAPI(title="Math Solver Service")

class QuadraticInput(BaseModel):
    a: float
    b: float
    c: float

@app.post("/api/math/solve/quadratic")
def solve_quadratic_equation(data: QuadraticInput):
    """Solves a quadratic equation ax^2 + bx + c = 0."""
    if data.a == 0:
        raise HTTPException(status_code=400, detail="Coefficient 'a' cannot be zero.")

    delta = (data.b**2) - (4*data.a*data.c)
    
    sol1 = (-data.b - cmath.sqrt(delta)) / (2*data.a)
    sol2 = (-data.b + cmath.sqrt(delta)) / (2*data.a)

    return {
        "input": {"a": data.a, "b": data.b, "c": data.c},
        "delta": delta,
        "solutions": {
            "x1": f"{sol1.real}{sol1.imag:+.4f}j" if sol1.imag != 0 else sol1.real,
            "x2": f"{sol2.real}{sol2.imag:+.4f}j" if sol2.imag != 0 else sol2.real,
        }
    }
