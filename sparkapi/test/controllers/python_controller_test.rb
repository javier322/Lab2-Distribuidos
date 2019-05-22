require 'test_helper'

class PythonControllerTest < ActionDispatch::IntegrationTest
  test "should get classifier" do
    get python_classifier_url
    assert_response :success
  end

end
