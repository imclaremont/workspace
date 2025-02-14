import requests
import pytest

def get_github_user_info(username: str) -> dict:
    """
    주어진 GitHub 사용자 이름(username)에 해당하는 정보를 가져와서 딕셔너리 형태로 반환합니다.
    정상적인 요청(200)일 경우 사용자 정보를 반환하며,
    그렇지 않을 경우 예외(ValueError)를 발생시킵니다.
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    # 상태 코드가 200(OK)이 아니면 예외 발생
    if response.status_code != 200:
        raise ValueError(
            f"GitHub API 에러 - 상태 코드: {response.status_code}, "
            f"메시지: {response.json().get('message', 'No message')}"
        )

    return response.json()


# ✅ 정상적인 GitHub 사용자 조회 테스트
def test_valid_username():
    username = "octocat"  # GitHub 공식 테스트용 계정
    user_info = get_github_user_info(username)

    assert "login" in user_info
    assert user_info["login"] == username


# ✅ 존재하지 않는 사용자일 경우 예외 발생 테스트
def test_invalid_username():
    invalid_username = "this_user_does_not_exist_abcxyz"

    with pytest.raises(ValueError) as excinfo:
        get_github_user_info(invalid_username)

    assert "GitHub API 에러" in str(excinfo.value)


# ✅ Mock을 활용한 정상 응답 테스트
def test_valid_username_mock(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "login": "mocked_user",
        "id": 123456,
        "name": "Mocked User"
    }

    mocker.patch("requests.get", return_value=mock_response)

    user_info = get_github_user_info("some_user")

    assert user_info["login"] == "mocked_user"
    assert user_info["id"] == 123456
    assert user_info["name"] == "Mocked User"


# ✅ Mock을 활용한 404 응답 테스트
def test_invalid_username_mock(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {"message": "Not Found"}

    mocker.patch("requests.get", return_value=mock_response)

    with pytest.raises(ValueError) as excinfo:
        get_github_user_info("invalid_user")

    assert "GitHub API 에러 - 상태 코드: 404" in str(excinfo.value)


if __name__ == "__main__":
    pytest.main()