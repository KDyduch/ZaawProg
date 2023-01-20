from fastapi import APIRouter
import sympy

prime_router = APIRouter()


@prime_router.get("/prime/{number}")
async def prime(number: int):
    isPrime = sympy.isprime(number)

    return {
        "is_prime": isPrime,
        "number": number,
    }
