/*
  This file is part of KDDockWidgets.

  SPDX-FileCopyrightText: 2020-2022 Klarälvdalens Datakonsult AB, a KDAB Group
  company <info@kdab.com> Author: Sérgio Martins <sergio.martins@kdab.com>

  SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

  Contact KDAB at <info@kdab.com> for commercial licensing options.
*/

#pragma once

#include "Controller.h"
#include "View.h"
#include "ViewWrapper_qtquick.h"

#include <QDebug>
#include <QEvent>
#include <QResizeEvent>
#include <QSizePolicy>
#include <QQuickItem>

#include <memory>

namespace KDDockWidgets::Views {

class DOCKS_EXPORT View_qtquick : public QQuickItem, public View
{
public:
    using View::close;
    using View::height;
    using View::minimumHeight;
    using View::minimumSizeHint;
    using View::minimumWidth;
    using View::rect;
    using View::resize;
    using View::width;

    explicit View_qtquick(KDDockWidgets::Controller *controller, Type type,
                          QQuickItem *parent = nullptr,
                          Qt::WindowFlags windowFlags = {});

    ~View_qtquick() override = default;

    void free_impl() override
    {
        // QObject::deleteLater();
        delete this;
    }

    QSize sizeHint() const override
    {
        return {};
    }

    QSize minSize() const override
    {
        return {};
    }

    QSize minimumSizeHint() const override
    {
        return {};
    }

    QSize maxSizeHint() const override
    {
        return {};
    }

    QSize maximumSize() const override
    {
        return {};
    }

    QRect geometry() const override
    {
        return {};
    }

    QRect normalGeometry() const override
    {
        return {};
    }

    void setGeometry(QRect geo) override
    {
    }

    void setMaximumSize(QSize) override
    {
    }

    bool isVisible() const override
    {
        return {};
    }

    void setVisible(bool) override
    {
    }

    void move(int x, int y) override
    {
        Q_UNUSED(x)
        Q_UNUSED(y)
    }

    void move(QPoint) override
    {
    }

    void setSize(int, int) override
    {
    }

    void setWidth(int) override
    {
    }

    void setHeight(int) override
    {
    }

    void setFixedWidth(int) override
    {
    }

    void setFixedHeight(int) override
    {
    }

    void show() override
    {
    }

    void hide() override
    {
    }

    void update() override
    {
    }

    void setParent(View *) override
    {
    }

    void raiseAndActivate() override
    {
    }

    void activateWindow() override
    {
    }

    void raise() override
    {
    }

    bool isTopLevel() const override
    {
        return {};
    }

    QPoint mapToGlobal(QPoint localPt) const override
    {
        return {};
    }

    QPoint mapFromGlobal(QPoint globalPt) const override
    {
        return {};
    }

    void setSizePolicy(QSizePolicy) override
    {
    }

    QSizePolicy sizePolicy() const override
    {
        return {};
    }

    void closeWindow() override
    {
    }

    QRect windowGeometry() const override
    {
        return {};
    }

    virtual QSize parentSize() const override
    {
        return {};
    }

    bool close() override
    {
        return {};
    }

    void setFlag(Qt::WindowType, bool = true) override
    {
    }

    void setAttribute(Qt::WidgetAttribute, bool = true) override
    {
    }

    bool testAttribute(Qt::WidgetAttribute) const override
    {
        return {};
    }

    Qt::WindowFlags flags() const override
    {
        return {};
    }

    void setWindowTitle(const QString &) override
    {
    }

    void setWindowIcon(const QIcon &) override
    {
    }

    bool isActiveWindow() const override
    {
        return {};
    }

    void showNormal() override
    {
    }

    void showMinimized() override
    {
    }

    void showMaximized() override
    {
    }

    bool isMinimized() const override
    {
        return {};
    }

    bool isMaximized() const override
    {
        return {};
    }

    QWindow *windowHandle() const override
    {
        return {};
    }

    HANDLE handle() const override
    {
        return reinterpret_cast<HANDLE>(this);
    }

    std::unique_ptr<ViewWrapper> window() const override
    {
        return {};
    }

    std::unique_ptr<ViewWrapper> parentView() const override
    {
        return {};
    }

    void setObjectName(const QString &) override
    {
    }

    void grabMouse() override
    {
    }

    void releaseMouse() override
    {
    }

    QScreen *screen() const override
    {
        return {};
    }

    void setFocus(Qt::FocusReason) override
    {
    }

    QString objectName() const override
    {
        return {};
    }

protected:
    bool event(QEvent *e) override
    {
        return QQuickItem::event(e);
    }

private:
    Q_DISABLE_COPY(View_qtquick)
};

} // namespace KDDockWidgets::Views
