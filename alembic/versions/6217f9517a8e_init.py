"""Init

Revision ID: 6217f9517a8e
Revises: 
Create Date: 2022-09-06 13:19:24.014924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6217f9517a8e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userdata')
    # ### end Alembic commands ###
