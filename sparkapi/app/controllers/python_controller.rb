class PythonController < ApplicationController
  skip_before_action :verify_authenticity_token



  def classifier
    @var = `python3.7 app/assets/lab2/classifier.py`


  end

  def classifier_post
    puts "****************************************1"
    # puts params[:_json].to_s.gsub(/"/,"'")
    # @list = params[:_json].to_s.gsub(/"/,"'")
    # puts @list.params
    puts params[:_json]
    @params=params[:_json]
    puts "****************************************2"

    # puts params[:_json].to_s.gsub(/"/,"'")
    @params2 = @params.to_s


    puts @params2

     # puts @params.to_s.gsub(/"/,"'")

    puts "****************************************3"
    @params3=  @params2.gsub("[<ActionController::Parameters ","")
    @params3=  @params3.gsub(" permitted: false>, <ActionController::Parameters",",")


    # @params4= @params3.gsub(" <ActionController::Parameters","")

    @params4= @params3.gsub(" permitted: false>]","")

    puts @params4
    puts "****************************************4"
    @params5 =  @params4.to_s.gsub(/"/,"'")
    @params5 =  @params5.to_s.gsub("=>",":")

    puts @params5
    puts "****************************************5"

      # puts element

      # if element == ("[#{@param5}]")
      #   "son iguales"
      # end

    @var = `python3.7 app/assets/lab2/classifier.py "#{@params5}"`

    puts @var.class

    respond_to do |format|

      format.json  { render :json => @var } # don't do msg.to_json
    end

  end
end
