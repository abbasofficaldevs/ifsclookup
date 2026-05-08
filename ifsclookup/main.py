import requests

API_URL = "https://ifsc.razorpay.com/{ifsc}"


def get_ifsc(ifsc_code: str) -> dict:
    """
    Fetch IFSC details from Razorpay IFSC API.

    Args:
        ifsc_code (str): Valid IFSC code

    Returns:
        dict: Bank information or error message
    """

    if not ifsc_code or not isinstance(ifsc_code, str):
        return {"error": "Invalid IFSC code"}

    try:
        response = requests.get(
            API_URL.format(ifsc=ifsc_code.strip().upper()),
            timeout=10
        )

        if response.status_code == 200:
            return response.json()

        return {
            "error": "IFSC not found",
            "status_code": response.status_code
        }

    except requests.RequestException as exc:
        return {"error": str(exc)}