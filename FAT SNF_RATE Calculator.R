library(shiny)

# Define UI
ui <- fluidPage(
  titlePanel("Fat & SNF Rate Calculator"),
  
  sidebarLayout(
    sidebarPanel(
      numericInput("fat", "Fat Percentage (%):", value = 4.0, min = 0, step = 0.1),
      numericInput("snf", "SNF Percentage (%):", value = 8.5, min = 0, step = 0.1),
      numericInput("fatRate", "Rate per unit Fat (₹):", value = 7.0, min = 0, step = 0.1),
      numericInput("snfRate", "Rate per unit SNF (₹):", value = 4.5, min = 0, step = 0.1),
      actionButton("calc", "Calculate")
    ),
    
    mainPanel(
      h4("Calculated Milk Rate (₹ per liter):"),
      verbatimTextOutput("milkRate")
    )
  )
)

# Define server logic
server <- function(input, output) {
  observeEvent(input$calc, {
    fat <- input$fat
    snf <- input$snf
    fatRate <- input$fatRate
    snfRate <- input$snfRate
    
    rate <- round(fat * fatRate + snf * snfRate, 2)
    
    output$milkRate <- renderText({
      paste("₹", rate)
    })
  })
}

# Run the application 
shinyApp(ui = ui, server = server)
