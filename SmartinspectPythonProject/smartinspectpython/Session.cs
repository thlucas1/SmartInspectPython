using static System.Net.Mime.MediaTypeNames;

"""
C# Methods with no equivalent Python functionality:

- public void ThreadExceptionHandler(object sender, ThreadExceptionEventArgs e)
  Acts as an event handler for the Application.ThreadException event.

- public void UnhandledExceptionHandler(object sender, UnhandledExceptionEventArgs e)
  Acts as an event handler for the AppDomain.UnhandledException event.

"""

    public class Session
    {


        /// <summary>
        Logs the tables of a DataSet instance with a
        custom log level.
        /// </summary>
        /// <param name="level">The log level of this method call.</param>
        /// <param name="dataSet">
        The DataSet instance whose tables should be logged.
        /// </param>
        /// <remarks>
        This method logs all tables of a DataSet instance by calling
        the LogDataTable method for every table.
        /// </remarks>
        public void LogDataSet(Level level, DataSet dataSet)
        {
            if (!IsOn(level))
                return;

            if (dataSet == null)
            {
                self.LogInternalError("LogDataSet: dataSet argument is null");
            }
            else
            {
                DataTableCollection? tables = dataSet.Tables;
                if (tables == null || tables.Count == 0)
                {
                    // Send an informative message that this
                    // dataset doesn't contain any tables at all.
                    LogMessage("The supplied DataSet object contains 0 tables.");
                }
                else
                {
                    if (tables.Count != 1)
                    {
                        // Send an informative message about the amount of
                        // tables in this dataset unless this dataset contains
                        // only one table. In the case of one table, this method
                        // will behave like any other method which sends only
                        // one Log Entry.

                        LogMessage(
                                "The supplied DataSet object contains {0} tables. " +
                                "The tables are listed below.", tables.Count
                            );
                    }

                    foreach (DataTable table in tables)
                    {
                        // Iterate through the entire table collection
                        // and log every table using the LogDataTable method.
                        LogDataTable(level, table.TableName, table);
                    }
                }
            }
        }


        /// <summary>
        Logs the content of a DataTable with a custom
        title and custom log level.
        /// </summary>
        /// <param name="level">The log level of this method call.</param>
        /// <param name="table">The table to log.</param>
        /// <param name="title">The title to display in the Console.</param>
        /// <remarks>
        <para>
        This method logs the content of the supplied table.
        </para>
        <para>
        LogDataTable is especially useful in database applications
        with lots of queries. It gives you the possibility to see the
        raw query results.
        </para>
        <para>
        See LogDataSet for a method which can handle more than one
        table at once.
        </para>
        /// </remarks>
        public void LogDataTable(Level level, string title, DataTable table)
        {
            if (self.IsOn(level))
            {
                if (table == null)
                {
                    self.LogInternalError("LogDataTable: table argument is null");
                }
                else
                {
                    // Just call the LogDataView method with
                    // the default view of the supplied table.
                    LogDataView(level, title, table.DefaultView);
                }
            }
        }



  
        /// <summary>
        Logs the table schemas of a DataSet instance with a custom log level.
        /// </summary>
        /// <param name="level">The log level of this method call.</param>
        /// <param name="dataSet">
        The DataSet instance whose table schemas should be logged.
        /// </param>
        /// <remarks>
        This method logs all table schemas of a DataSet instance
        by calling the LogDataTableSchema method for every table.
        /// </remarks>
        public void LogDataSetSchema(Level level, DataSet dataSet)
        {
            if (!IsOn(level))
                return;

            if (dataSet == null)
            {
                self.LogInternalError("LogDataSetSchema: dataSet argument is null");
            }
            else
            {
                DataTableCollection? tables = dataSet.Tables;
                if (tables == null || tables.Count == 0)
                {
                    // Send an informative message that this
                    // dataset doesn't contain any tables at all.
                    LogMessage("The supplied DataSet object contains 0 tables.");
                }
                else
                {
                    if (tables.Count != 1)
                    {
                        // Send an informative message about the amount of
                        // tables in this dataset unless this dataset contains
                        // only one table. In the case of one table, this method
                        // will behave like any other method which sends only one
                        // Log Entry.

                        LogMessage(
                                "The supplied DataSet object contains {0} tables. " +
                                "The schemas are listed below.", tables.Count
                            );
                    }

                    foreach (DataTable table in tables)
                    {
                        // Iterate through the entire table collection and log
                        // every table schema using the LogDataTableSchema method.
                        LogDataTableSchema(level, table.TableName, table);
                    }
                }
            }
        }







        /// <summary>
        Logs the content of a DataView with a custom title and custom log level.
        /// </summary>
        /// <param name="level">The log level of this method call.</param>
        /// <param name="title">The title to display in the Console.</param>
        /// <param name="dataview">The data view to log.</param>
        /// <remarks>
        <para>
        This method logs the content of the supplied data view.
        </para>
        <para>
        LogDataView is especially useful in database applications
        with lots of queries. It gives you the possibility to see the
        raw query results.
        </para>
        ///	</remarks>
        public void LogDataView(Level level, string title, DataView dataview)
        {
            if (!IsOn(level))
                return;

            if (dataview == null || dataview.Table == null)
            {
                self.LogInternalError("LogDataView: dataview or related table is null");
                return;
            }

            DataColumnCollection columns = dataview.Table.Columns;

            if (columns == null)
            {
                self.LogInternalError("LogDataView: table argument contains no columns");
                return;
            }

            TableViewerContext ctx = new TableViewerContext();
            try
            {
                ctx.BeginRow();
                try
                {
                    // We need to write the headers of the
                    // table, that means, the names of the columns.
                    for (int i = 0, count = columns.Count; i < count; i++)
                    {
                        ctx.AddRowEntry(columns[i].ColumnName);
                    }
                }
                finally
                {
                    ctx.EndRow();
                }

                // After we've written the table header, we
                // can now write the whole dataview content.
                foreach (DataRowView rowview in dataview)
                {
                    ctx.BeginRow();
                    try
                    {
                        // For every row in the view we need to iterate through
                        // the columns and need to extract the related field value.
                        for (int i = 0, count = columns.Count; i < count; i++)
                        {
                            object field = rowview[i];

                            if (field != null)
                            {
                                // Add the field to the current row.
                                ctx.AddRowEntry(field.ToString());
                            }
                        }
                    }
                    finally
                    {
                        ctx.EndRow();
                    }
                }

                self.SendContext(level, title, LogEntryType.DatabaseResult, ctx);
            }
            catch (Exception e)
            {
                self.LogInternalError("LogDataView: " + e.Message);
            }
        }





  /// <overloads>
  Tracks a method.
  /// </overloads>
  /// <summary>
  Tracks a method by using the default log level.
  /// </summary>
  /// <param name="methodName">The name of the method.</param>
  /// <returns>
  A MethodTracker object.
        /// </returns>
        /// <remarks>
        <para>

  The TrackMethod method notifies the Console that a new
  method has been entered.The returned MethodTracker object
  can be wrapped in a using statement and then automatically
  calls LeaveMethod on disposal.
        </para>
        <para>
        This method uses the<see cref="SmartInspect.DefaultLevel"/>
        of the session's <see cref="Parent"/> as log
        level.For more information, please refer to the documentation
        of the<see cref="SmartInspect.DefaultLevel"/> property
        of the <see cref = "SmartInspect" /> class..
        </para>
        /// </remarks>
        public MethodTracker? TrackMethod(string methodName)
  {
    return self.TrackMethod(self.fParent.DefaultLevel, methodName);
  }

  /// <summary>
  Tracks a method by using a custom log level.
  /// </summary>
  /// <param name="level">The log level of this method call.</param>
  /// <param name="methodName">The name of the method.</param>
  /// <returns>
  A MethodTracker object.
        /// </returns>
        /// <remarks>
        The TrackMethod method notifies the Console that a new
        method has been entered.The returned MethodTracker object
        can be wrapped in a using statement and then automatically
        calls LeaveMethod on disposal.
        /// </remarks>
        public MethodTracker? TrackMethod(Level level, string methodName)
  {
    if (self.IsOn(level))
      return new MethodTracker(level, this, methodName);
    else
      return null;
  }

  /// <summary>
  Tracks a method by using the default log level.
  The method name consists of a format string and the related

  array of arguments.
  /// </summary>
  /// <param name="methodNameFmt">
  The format string to create the name of the method.
        /// </param>
        /// <param name="args">
  The array of arguments for the format string.
        /// </param>
        /// <returns>
  A MethodTracker object.
        /// </returns>
        /// <remarks>
        <para>

  The TrackMethod method notifies the Console that a new
  method has been entered.The returned MethodTracker object
  can be wrapped in a using statement and then automatically
  calls LeaveMethod on disposal.
        </para>
        <para>
        The resulting method name consists of a format string and the
        related array of arguments.
        </para>
        <para>
        This method uses the<see cref="SmartInspect.DefaultLevel"/>
        of the session's <see cref="Parent"/> as log
        level.For more information, please refer to the documentation
        of the<see cref="SmartInspect.DefaultLevel"/> property
        of the <see cref = "SmartInspect" /> class..
        </para>
        /// </remarks>
        public MethodTracker? TrackMethod(string methodNameFmt, object[] args)
  {
    return self.TrackMethod(self.fParent.DefaultLevel, methodNameFmt, args);
  }

  /// <summary>
  Tracks a method by using a custom log level.
  The method name consists of a format string and the related
        array of arguments.
        /// </summary>
        /// <param name="level">The log level of this method call.</param>
        /// <param name="methodNameFmt">
        The format string to create the name of the method.
  /// </param>
  /// <param name="args">
        The array of arguments for the format string.
        /// </param>
        /// <returns>
        A MethodTracker object.
        /// </returns>
        /// <remarks>
        <para>
        The TrackMethod method notifies the Console that a new
        method has been entered.The returned MethodTracker object
        can be wrapped in a using statement and then automatically
        calls LeaveMethod on disposal.
        </para>
        <para>
        The resulting method name consists of a format string and the
        related array of arguments.
        </para>
        /// </remarks>
        public MethodTracker? TrackMethod(Level level, string methodNameFmt, object[] args)
  {
    if (self.IsOn(level))
    {
      try
      {
        return self.TrackMethod(level, String.Format(methodNameFmt, args));
      }
      catch (Exception e)
      {
        self.LogInternalError("TrackMethod: " + e.Message);
      }
    }

    return null;
  }

  /// <summary>
  Tracks a method by using the default log level.
  The resulting method name consists of the FullName of the
  type of the supplied instance parameter, followed by a dot

  and the supplied methodName argument.
  /// </summary>
  /// <param name="methodName">The name of the method.</param>
  /// <param name="instance">
  The class name of this instance and a dot will be prepended
  to the method name.
  /// </param>
  /// <returns>
  A MethodTracker object.
        /// </returns>
        /// <remarks>
        <para>

  The TrackMethod method notifies the Console that a new
  method has been entered.The returned MethodTracker object
  can be wrapped in a using statement and then automatically
  calls LeaveMethod on disposal.
        </para>
        <para>
        The resulting method name consists of the FullName of the type
        of the supplied instance parameter, followed by a dot and the
        supplied methodName argument.
        </para>
        <para>
        This method uses the <see cref = "SmartInspect.DefaultLevel" />
        of the session's <see cref="Parent"/> as log
        level.For more information, please refer to the documentation
        of the<see cref="SmartInspect.DefaultLevel"/> property
        of the <see cref = "SmartInspect" /> class..
        </para>
        /// </remarks>
        public MethodTracker? TrackMethod(object instance, string methodName)
  {
    return self.TrackMethod(self.fParent.DefaultLevel, instance, methodName);
  }

  /// <summary>
  Tracks a method by using a custom log level.
  The resulting method name consists of the FullName of the
        type of the supplied instance parameter, followed by a dot
        and the supplied methodName argument.
        /// </summary>
        /// <param name="level">The log level of this method call.</param>
        /// <param name="methodName">The name of the method.</param>
        /// <param name="instance">
        The class name of this instance and a dot will be prepended
        to the method name.
        /// </param>
        /// <returns>
        A MethodTracker object.
        /// </returns>
        /// <remarks>
        <para>
        The TrackMethod method notifies the Console that a new
        method has been entered.The returned MethodTracker object
        can be wrapped in a using statement and then automatically
        calls LeaveMethod on disposal.
        </para>
        <para>
        The resulting method name consists of the FullName of the type
        of the supplied instance parameter, followed by a dot and the
        supplied methodName argument.
        </para>
        /// </remarks>
        public MethodTracker? TrackMethod(Level level, object instance, string methodName)
  {
    if (self.IsOn(level))
    {
      if (instance == null)
      {
        self.LogInternalError("TrackMethod: instance argument is null");
      }
      else
      {
        string? type = instance.GetType().FullName;
        return self.TrackMethod(level, type + "." + methodName);
      }
    }

    return null;
  }

  /// <summary>
  Tracks a method by using the default log level.
  The resulting method name consists of the FullName of the
  type of the supplied instance parameter, followed by a dot

  and the supplied format string and its related array of

  arguments.
  /// </summary>
  /// <param name="instance">
  The class name of this instance and a dot will be prepended
  to the method name.
  /// </param>
  /// <param name="methodNameFmt">
  The format string to create the name of the method.
        /// </param>
        /// <param name="args">
  The array of arguments for the format string.
        /// </param>
        /// <returns>
  A MethodTracker object.
        /// </returns>
        /// <remarks>
        <para>

  The TrackMethod method notifies the Console that a new
  method has been entered.The returned MethodTracker object
  can be wrapped in a using statement and then automatically
  calls LeaveMethod on disposal.
        </para>
        <para>
        The resulting method name consists of the FullName of the
        type of the supplied instance parameter, followed by a dot and
        the supplied format string and its related array of arguments.
        </para>
        <para>
        This method uses the<see cref="SmartInspect.DefaultLevel"/>
        of the session's <see cref="Parent"/> as log
        level.For more information, please refer to the documentation
        of the<see cref="SmartInspect.DefaultLevel"/> property
        of the <see cref = "SmartInspect" /> class..
        </para>
        /// </remarks>
        public MethodTracker? TrackMethod(object instance, string methodNameFmt, object[] args)
  {
    return self.TrackMethod(self.fParent.DefaultLevel, instance, methodNameFmt, args);
  }

  /// <summary>
  Tracks a method by using a custom log level.
  The resulting method name consists of the FullName of the
        type of the supplied instance parameter, followed by a dot
        and the supplied format string and its related array of
        arguments.
        /// </summary>
        /// <param name="level">The log level of this method call.</param>
        /// <param name="instance">
        The class name of this instance and a dot will be prepended
        to the method name.
        /// </param>
        /// <param name="methodNameFmt">
        The format string to create the name of the method.
        /// </param>
        /// <param name="args">
        The array of arguments for the format string.
        /// </param>
        /// <returns>
        A MethodTracker object.
        /// </returns>
        /// <remarks>
        <para>
        The TrackMethod method notifies the Console that a new
        method has been entered.The returned MethodTracker object
        can be wrapped in a using statement and then automatically
        calls LeaveMethod on disposal.
        </para>
        <para>
        The resulting method name consists of the FullName of the
        type of the supplied instance parameter, followed by a dot and
        the supplied format string and its related array of arguments.
        </para>
        /// </remarks>
        public MethodTracker? TrackMethod(Level level, object instance, string methodNameFmt, object[] args)
  {
    if (self.IsOn(level))
    {
      if (instance == null)
      {
        self.LogInternalError("TrackMethod: instance argument is null");
      }
      else
      {
        try
        {
          return self.TrackMethod(
                  level,
                  instance.GetType().FullName + "." +
                  String.Format(methodNameFmt, args)
              );
        }
        catch (Exception e)
        {
          self.LogInternalError("TrackMethod: " + e.Message);
        }
      }
    }

    return null;
  }