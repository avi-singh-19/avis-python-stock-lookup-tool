from final_project import export_data_to_csv, create_graph_as_png


def test_take_in_stock_price_valid_ticker(valid_yf_api_call):  # tests function 1 API can gather data
    # arrange and act
    response = valid_yf_api_call
    # assert
    assert response.empty == False


def test_take_in_stock_price_invalid_ticker(invalid_yf_api_call):  # tests function 1 API rejects invalid ticker
    # arrange and act
    response = invalid_yf_api_call
    # assert
    assert response.empty == True


def test_export_data_to_csv(valid_yf_api_call, matching_yf_api_ticker): # tests function 2 writes valid data to file
    # arrange and act
    result = export_data_to_csv(valid_yf_api_call, matching_yf_api_ticker)
    # assert
    assert result == ('Data written to file', True)


def test_create_graph_as_png(valid_yf_api_call, matching_yf_api_ticker): # tests function 3 writes valid png to file
    # arrange and act
    result = create_graph_as_png(valid_yf_api_call, matching_yf_api_ticker)
    # assert
    assert result == ('Graph saved to file', True)