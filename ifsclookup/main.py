import requests

API_URL = "https://ifsc.razorpay.com/{}"


def get_ifsc(ifsc_code: str) -> dict:
    """
    Fetch IFSC details.

    Args:
        ifsc_code (str): Bank IFSC code

    Returns:
        dict: Bank details or error
    """

    if not isinstance(ifsc_code, str) or not ifsc_code.strip():
        return {
            "success": False,
            "error": "Invalid IFSC code"
        }

    ifsc_code = ifsc_code.strip().upper()

    try:
        response = requests.get(
            API_URL.format(ifsc_code),
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()

            return {
                "success": True,
                "data": data
            }

        return {
            "success": False,
            "error": "IFSC not found",
            "status_code": response.status_code
        }

    except requests.RequestException as e:
        return {
            "success": False,
            "error": str(e)
        }
