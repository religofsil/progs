library(shiny)

# Define a server for the Shiny app
shinyServer(function(input, output) {
  
  # Filter data based on selections
  output$table <- DT::renderDataTable(DT::datatable({
    data <- read.csv("http://hsequantling.wikispaces.com/file/view/all_words.csv", encoding = "UTF-8")
    if (input$language != "All") {
      data <- data[data$language == input$language,]
    }
    data
  }))
  
})