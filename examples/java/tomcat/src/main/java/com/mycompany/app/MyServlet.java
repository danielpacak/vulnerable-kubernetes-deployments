package com.mycompany.app;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class MyServlet extends HttpServlet {

    @Override
    protected void doGet(
            HttpServletRequest req,
            HttpServletResponse resp) throws IOException {

        resp.setStatus(HttpServletResponse.SC_OK);
        resp.getWriter().write("test");
        resp.getWriter().flush();
        resp.getWriter().close();
    }
}
